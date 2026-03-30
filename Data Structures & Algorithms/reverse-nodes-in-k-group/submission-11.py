# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        dummy = ListNode(0,head)
        groupPrev = dummy

        while True:
            kth = self.getkth(groupPrev, k)
            if not kth:
                break
            groupNext = kth.next
            # reverse 
            
            curr, prev = groupPrev.next, kth.next

            while curr != groupNext:
                curr.next, prev, curr = prev, curr, curr.next

            # update
            groupPrev.next,groupPrev  =  kth,groupPrev.next
        return dummy.next

    def getkth(self, curr, k):

        while k > 0 and curr:
            curr = curr.next
            k -=1
        return curr
        