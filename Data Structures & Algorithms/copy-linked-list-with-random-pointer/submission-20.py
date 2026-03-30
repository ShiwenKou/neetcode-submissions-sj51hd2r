"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        mappings = {None:None}
        dummy = Node(0, head)
        curr = dummy.next
        while curr:
            copy = Node(curr.val)
            mappings[curr] = copy
            curr = curr.next
        curr = dummy.next
        while curr:
            copy = mappings[curr]
            copy.next = mappings[curr.next]
            copy.random = mappings[curr.random]
            curr = curr.next
        
        return mappings[head]
        