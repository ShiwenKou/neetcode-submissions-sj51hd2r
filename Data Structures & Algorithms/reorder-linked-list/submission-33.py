# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        if not head or not head.next:
            return
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        middle = slow
        first, second, middle.next = head, middle.next, None
        # reverse
        curr, prev = second, None
        while curr:
            curr.next, prev, curr = prev, curr, curr.next
        second = prev
        # merge
        while second:
            first.next, second.next, first, second = second, first.next, first.next, second.next
        