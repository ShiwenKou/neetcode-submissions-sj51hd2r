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
        mappings = {}

        def dfs(node):
            mappings[node] = Node(node.val)
            for nei in node.neighbors:
                if nei not in mappings:
                    dfs(nei)
        dfs(node)
        for oldNode, newNode in mappings.items():
            for nei in oldNode.neighbors:
                newNode.neighbors.append(mappings[nei])
        return mappings[node]