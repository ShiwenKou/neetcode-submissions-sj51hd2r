# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        # find k
        # stitch
        #reverse
        # remaining less than k, break
        dummy = ListNode(0, head)
        groupPrev = dummy
        while True:
            kth = self.findkth(groupPrev, k)
            if not kth:
                break
            
            groupNext = kth.next

            curr, prev = groupPrev.next, groupNext
            # reverse
            while curr != groupNext:
                curr.next, prev, curr = prev, curr, curr.next
            
            # updating pointers

            groupPrev.next, groupPrev = kth, groupPrev.next
        return dummy.next


    def findkth(self, curr, k):

        while k and curr:
            curr = curr.next
            k -= 1
        return curr
        