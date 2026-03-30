# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        # find middle, split, reverse, merge

        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        slow.next, second = None, slow.next

        curr, prev = second, None
        while curr:
            curr.next, prev, curr = prev, curr, curr.next
        
        second, first = prev, head

        while second:
            first.next, second.next, first, second = second, first.next,first.next, second.next

