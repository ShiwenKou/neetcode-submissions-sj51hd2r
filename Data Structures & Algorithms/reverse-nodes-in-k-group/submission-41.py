# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        

        def findKth(curr, k):
            n = k

            while n and curr:
                curr = curr.next
                n -= 1

            return curr
        dummy = ListNode(0, head)
        groupPrev = dummy
        while True:

            kth = findKth(groupPrev, k)
            if not kth:
                break
            groupNext = kth.next

            cur, prev = groupPrev.next, groupNext

            while cur != groupNext:
                cur.next, prev, cur = prev, cur, cur.next

            groupPrev.next, groupPrev = kth, groupPrev.next

        return dummy.next
            