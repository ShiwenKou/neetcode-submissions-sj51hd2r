# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        # find middle, split, reverse, merge
        # if not head or not head.next:
        #     return head
        
        slow, fast = head, head.next
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        second, slow.next = slow.next, None
        prev, curr = None, second
        while curr:
            curr.next, prev, curr = prev, curr, curr.next
        second = prev
        first = head
        while second:
            first.next, second.next, first, second = second, first.next, first.next, second.next

        