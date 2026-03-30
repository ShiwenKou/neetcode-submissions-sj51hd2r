# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False
        st = set()

        while head.next and head:

            if head.val in st:
                return True
            else:
                st.add(head.val)
                head = head.next
        return False


        
        