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
        
        mappings = {None: None}

        cur = head

        while cur:
            copy = Node(cur.val)
            mappings[cur] = copy
            cur = cur.next

        cur = head

        while cur:
            copy = mappings[cur]
            copy.next = mappings[cur.next]
            copy.random = mappings[cur.random]
            cur = cur.next

        return mappings[head]