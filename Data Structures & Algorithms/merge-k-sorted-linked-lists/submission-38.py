# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        if not lists:
            return None

        def mergeList(l1, l2):
            dummy = ListNode()
            curr = dummy

            while l1 and l2:
                if l1.val < l2.val:
                    curr.next = l1
                    l1 = l1.next
                else:
                    curr.next = l2
                    l2 = l2.next
                curr = curr.next
            if l1:
                curr.next = l1
            if l2:
                curr.next = l2
            return dummy.next

        
        length = len(lists)

        while length > 1:
            j = 0
            for i in range(0, length, 2):
                list1 = lists[i]
                list2 = lists[i + 1] if i + 1 < length else None

                lists[j] = mergeList(list1, list2)
                j += 1
            
            length = j
        return lists[0]