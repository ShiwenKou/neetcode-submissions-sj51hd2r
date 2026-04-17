# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        dummy = head

        fast, slow = dummy, dummy

        while fast and fast.next: # find middle
            fast = fast.next.next
            slow = slow.next
        middle = slow

        first, second, middle.next = head, middle.next, None # split

        # reverse

        cur, prev = second, None
        while cur:
            cur.next, prev, cur = prev, cur, cur.next
        # merge

        second = prev

        while second:
            first.next, second.next, first, second = second, first.next, first.next, second.next




