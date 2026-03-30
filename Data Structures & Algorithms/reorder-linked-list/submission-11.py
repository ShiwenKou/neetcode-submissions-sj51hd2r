# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

       
        dummy = ListNode(0,head)

        fast= slow = dummy

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second, slow.next = slow.next, None

        # reverse
        curr, prev = second, None
        while curr:
            curr.next, prev, curr = prev, curr, curr.next
        
        # merge
        first, second = head, prev
        while second:

            first.next, second.next, first, second = second, first.next, first.next, second.next






