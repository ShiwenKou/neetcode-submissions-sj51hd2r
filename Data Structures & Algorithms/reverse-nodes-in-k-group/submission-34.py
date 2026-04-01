# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        # find kth
        # split, make 1 connected to 4
        # reverse
        # merge

        def findKth(curr, k):
            while k > 0 and curr:
                curr = curr.next
                k -= 1
            return curr
        dummy = ListNode(0, head)
        groupPrev = dummy
        while True:
            
            kth = findKth(groupPrev, k)
            if kth == None:
                break

            groupNext = kth.next

            curr, prev = groupPrev.next, groupNext

            while curr != groupNext:
                curr.next, prev, curr = prev, curr, curr.next
            
            # update groupPrev, and groupPrev.next
            groupPrev.next, groupPrev = kth, groupPrev.next
        return dummy.next

