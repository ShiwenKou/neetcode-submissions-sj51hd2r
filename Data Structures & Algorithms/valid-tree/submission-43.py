class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        # this is undirected graph, so we need a visited set and a prev node


        visited = set()

        adjList = collections.defaultdict(list)

        for n1, n2 in edges:

            adjList[n1].append(n2)
            adjList[n2].append(n1)
        def dfs(cur, prev):

            if cur in visited:
                return False

            visited.add(cur)

            for nei in adjList[cur]:
                if nei != prev:

                    if dfs(nei, cur) == False:
                        return False
            return True

        ans = dfs(0, -1)
        if ans == False:
            return False
        else:
            return len(visited) == n