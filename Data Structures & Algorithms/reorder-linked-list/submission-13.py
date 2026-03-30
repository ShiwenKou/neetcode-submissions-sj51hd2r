# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # this problem is not hard, actually i should do this one often. cuz it can help me review so many related linked list problems.


        # so no we need to find the middle node here. it's easy, we use a two pointer technique.

        dummy = ListNode(0,head)

        fast = slow = dummy

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # slow will be in middle

        slow.next, Second = None, slow.next

        # reverse the second linked list
        prev, curr = None, Second

        while curr:
            curr.next, prev, curr = prev, curr, curr.next

        # prev is the start of the reversed linked list

        # merge
        First, Second = head, prev
        while Second:

            First.next, Second.next, First, Second = Second, First.next, First.next, Second.next
        

