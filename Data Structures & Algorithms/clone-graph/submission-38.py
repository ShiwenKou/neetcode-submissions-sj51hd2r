"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        mappings = collections.defaultdict(list)
        dq = collections.deque()
        dq.append(node)

        while dq:

            cur = dq.popleft()
            mappings[cur] = Node(cur.val)
            for nei in cur.neighbors:
                if nei not in mappings:
                    dq.append(nei)
        
        for oldNode, newNode in mappings.items():
            for nei in oldNode.neighbors:
                newNode.neighbors.append(mappings[nei])
        return mappings[node]