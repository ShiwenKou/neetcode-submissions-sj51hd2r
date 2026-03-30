# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        dummy = ListNode(0, head)
        slow = fast = dummy

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
 
        # slow here is the dummy to the second linkedlist
        curr = slow.next
        slow.next = None

        # reverse the second list
        prev = None
        
        while curr:
            curr.next,prev, curr = prev, curr, curr.next

        # now the start of the second linked list is prev
        # merge
        first = dummy.next
        second = prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2


        