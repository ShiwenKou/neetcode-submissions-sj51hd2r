class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        

        # undirect graph, can use union find or track prev 
        adjList = collections.defaultdict(list)
        for n1, n2 in edges:
            adjList[n1].append(n2)
            adjList[n2].append(n1)
        seen = set()
        def dfs(curr, prev):

            if curr in seen:
                return False

            seen.add(curr)
            for nei in adjList[curr]:
                if nei == prev:
                    continue
                if dfs(nei, curr) == False:
                    return False # a loop detected
            
            return True
        return dfs(0, -1) and len(seen) == n