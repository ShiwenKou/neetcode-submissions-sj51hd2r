class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjList = collections.defaultdict(list)

        for n1, n2 in edges:
            adjList[n1].append(n2)
            adjList[n2].append(n1)
        seen = set()
        def dfs(node):

            if node in seen:
                return
            seen.add(node)

            for nei in adjList[node]:
                    dfs(nei)


        total = 0

        for node in range(n):
            if node not in seen:
                total += 1
                dfs(node)
        return total