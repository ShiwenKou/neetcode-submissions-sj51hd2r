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
        
        mappings = {None : None}


        cur = head

        while cur:
            copy = Node(cur.val)
            mappings[cur] = copy
            cur = cur.next
        
        cur = head

        for node, copy in mappings.items():
            if not node:
                continue
            copy.next = mappings[node.next]
            copy.random = mappings[node.random]
        return mappings[head]