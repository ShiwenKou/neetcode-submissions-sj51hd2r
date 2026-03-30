# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next: # null or only one ndoe:
            return

        middle = self.findMiddle(head)

        first, second, middle.next = head, middle.next, None

        # reveres

        curr, prev = second, None
        while curr:
            curr.next, prev, curr = prev, curr, curr.next
        
        # merge

        second = prev

        while second:
            first.next, second.next, first, second = second, first.next, first.next, second.next



    def findMiddle(self, head):
        fast, slow = head.next, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
        