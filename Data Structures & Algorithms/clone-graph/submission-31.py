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
        dq = collections.deque()

        dq.append(node)
        clone = {}
        while dq:
            
            curr = dq.popleft()

            clone[curr] = Node(curr.val)


            for nei in curr.neighbors:
                if nei not in clone:
                    dq.append(nei)

        
        for oldNode, newNode in clone.items():
            for nei in oldNode.neighbors:
                newNode.neighbors.append(clone[nei])
            
        return clone[node]