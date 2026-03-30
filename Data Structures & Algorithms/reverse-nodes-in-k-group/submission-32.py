# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # find k, reverse,  if less than k, return
        dummy = ListNode(0, head)
        groupPrev = dummy
        while True:
            kth = self.findKth(groupPrev, k)
            if not kth:
                break
            groupNext = kth.next

            curr = groupPrev.next
            prev = groupNext
            while curr != groupNext:
                curr.next, prev, curr = prev, curr, curr.next
            # update pointers

            groupPrev.next, groupPrev = kth, groupPrev.next
        return dummy.next

    def findKth(self, curr, k):

        while k and curr:
            curr = curr.next
            k -= 1
        return curr
        