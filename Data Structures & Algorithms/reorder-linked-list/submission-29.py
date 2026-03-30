# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        # find middle - split, reverse, merge again

        if not head or not head.next:
            return
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        middle = slow
        first , second, middle.next = head, middle.next, None

        # reverse from second
        curr = second
        prev = None
        while curr:
            curr.next, prev, curr = prev, curr, curr.next
        
        second = prev

        while second:
            first.next, second.next, first, second = second, first.next, first.next, second.next
        

        