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

        curr = head
        while curr:
            val = curr.val
            copy = Node(val)
            mappings[curr] = copy
            curr = curr.next
        
        curr = head
        while curr:
            copy = mappings[curr]

            copy.next = mappings[curr.next]
            copy.random = mappings[curr.random]
            curr = curr.next
        return mappings[head]
        