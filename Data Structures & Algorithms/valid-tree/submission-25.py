class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        # undirected graph
        # no loop. one component

        # use prev
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
                    if dfs(nei, node) == False:
                        return False
            return True

        
        if dfs(0, -1) == False:
            return False
        
        if len(visited) != n:
            return False
        return True

