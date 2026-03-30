# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        st = set()

        if not head or not head.next:
            return False

        while head:
            if head in st:
                return True
            else:
                st.add(head)
            head = head.next
        return False