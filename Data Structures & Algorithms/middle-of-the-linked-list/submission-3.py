# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        dummy_head = head
        lst = []
        while head:

            lst.append(head)

            head = head.next


        if len(lst) % 2 == 0:
            return lst[math.ceil((0 + len(lst) - 1) /2)]
        else:
            return lst[(0 + len(lst) - 1) //2]
