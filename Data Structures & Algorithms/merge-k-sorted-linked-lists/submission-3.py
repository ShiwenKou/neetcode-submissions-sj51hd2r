# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None

        

        while len(lists) > 1:
            sortedList = []
            for i in range(0,len(lists),2):

                l1 = lists[i]
                l2 = lists[i + 1] if len(lists) > i+1 else None

                sortedList.append(self.mergeList(l1,l2))
            lists = sortedList
        return lists[0]

    def mergeList(self, left, right):
        dummy = ListNode()
        curr = dummy

        while left and right:
            if left.val < right.val:
                curr.next = left
                left = left.next
            else:
                curr.next = right
                right = right.next
            curr = curr.next

        if left:
            curr.next = left
        if right:
            curr.next = right
        return dummy.next

        