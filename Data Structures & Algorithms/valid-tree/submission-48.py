class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        

        # one component, no loops

        adjList = collections.defaultdict(list)

        for n1, n2 in edges:
            adjList[n1].append(n2)
            adjList[n2].append(n1)
        visited = set()
        def dfs(curr, prev):

            if curr in visited:
                return False
            visited.add(curr)

            for nei in adjList[curr]:
                if nei != prev:
                    if not dfs(nei, curr):
                        return False

            return True

        ans = dfs(0, -1)

        return ans if len(visited) == n else False 