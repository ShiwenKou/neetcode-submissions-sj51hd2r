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
        stack = []
        stack.append(node)
        mappings = {}
        mappings[node] = Node(node.val)

        while stack:
            curr = stack.pop()
            for nei in curr.neighbors:
                if nei not in mappings:
                    stack.append(nei)
                    mappings[nei] = Node(nei.val)
        
        for oldNode, newNode in mappings.items():
            for nei in oldNode.neighbors:
                newNode.neighbors.append(mappings[nei])
        return mappings[node]