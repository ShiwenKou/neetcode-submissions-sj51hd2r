class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # one component
        # no loops


        adjList = collections.defaultdict(list)
        for n1, n2 in edges:
            adjList[n1].append(n2)
            adjList[n2].append(n1)


        seen = set()

        def dfs(node, prev):

            if node in seen:
                return False

            seen.add(node)

            for nei in adjList[node]:
                if nei == prev:
                    continue
                
                if not dfs(nei, node):
                    return False
            return True

        
        ans = dfs(0, -1)
        return ans if len(seen) == n else False
            