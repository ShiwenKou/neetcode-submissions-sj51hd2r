class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjList = collections.defaultdict(list)
        for n1, n2 in edges:
            adjList[n1].append(n2)
            adjList[n2].append(n1)
        
        cycle = set()



        def dfs(node, prev):

            if node in cycle:
                return False # loop detected
            
            cycle.add(node)

            for nei in adjList[node]:
                if nei != prev:
                    if dfs(nei, node) == False:
                        return False
            return True

        
        ans = dfs(0, -1)

        return ans if len(cycle) == n else False