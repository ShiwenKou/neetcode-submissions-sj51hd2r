class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # this is a undirected graph. so immediately we know we can use dfs with prev passed in
        # or union find

        # a tree -> no loops, one conponent
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
                if dfs(nei, node) == False:
                    return False
            return True

        # if this is a tree, called once, all nodes in seen
        return dfs(0, -1) and len(seen) == n