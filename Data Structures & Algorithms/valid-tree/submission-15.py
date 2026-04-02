class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        adjList = collections.defaultdict(list)

        for n1, n2 in edges:
            adjList[n1].append(n2)
            adjList[n2].append(n1)
        # so we have a adjacency list now can do dfs

        # cycle for loops down the path, and a seen to expidite the desicion

        cycle = set()
        seen = set()

        def dfs(node, prev):
            if node in cycle:
                return False
            
            cycle.add(node)

            for nei in adjList[node]:
                if nei != prev:
                    if dfs(nei, node) == False:
                        return False
            # cycle.remove(node)
            seen.add(node)
            return True
        # len(seen) is the node we see so far, if len(seen) != n, means more than one compoments

        res = dfs(0, -1)
        if len(seen) == n:
            return res
        
        else:
            return False