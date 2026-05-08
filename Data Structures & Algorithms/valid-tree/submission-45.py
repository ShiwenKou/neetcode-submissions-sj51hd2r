class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # this is a undirected tree, so we need to keep track of a prev node

        adjList = collections.defaultdict(list)
        for n1, n2 in edges:
            adjList[n1].append(n2)
            adjList[n2].append(n1)

        visited = set()

        def dfs(node, prev):
            if node in visited:
                return False

            visited.add(node)

            for nei in adjList[node]:
                if nei != prev:
                    if not dfs(nei, node):
                        return False # a loop is detected

            return True # node has no neighbors
        
        if not dfs(0, -1):
            return False
        
        return len(visited) == n



