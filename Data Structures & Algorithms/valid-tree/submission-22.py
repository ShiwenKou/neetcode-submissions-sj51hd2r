class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        # no cycle, one component
        adjList = collections.defaultdict(list)
        for n1, n2 in edges:
            adjList[n1].append(n2)
            adjList[n2].append(n1)
        

        seen = set() # detect loops

        def dfs(node, prev):

            if node in seen:
                return False
            
            seen.add(node)

            for nei in adjList[node]:
                if nei != prev:
                    if dfs(nei, node) == False:
                        return False
            return True

        res = dfs(0, -1)

        if len(seen) == n:
            return res
        
        else:
            return False