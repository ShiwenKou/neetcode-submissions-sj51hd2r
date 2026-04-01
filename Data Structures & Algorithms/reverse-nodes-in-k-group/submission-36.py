# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        

        def findKth(curr, n):
            while curr and n:
                curr = curr.next
                n -= 1
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
            
            groupPrev.next, groupPrev = kth, groupPrev.next
        
        return dummy.next



