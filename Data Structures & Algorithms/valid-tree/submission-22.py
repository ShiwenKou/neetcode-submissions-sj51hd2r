class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        # undirected graph, should check prev
        adjList = collections.defaultdict(list)
        for n1, n2 in edges:
            adjList[n1].append(n2)
            adjList[n2].append(n1)

        seen = set()
        def dfs(node, prev):

            if node in seen:
                return False # a loop detected
            seen.add(node)

            for nei in adjList[node]:
                if nei != prev:
                    if dfs(nei, node) == False:
                        return False

            return True


        return dfs(0, - 1) and len(seen) == n