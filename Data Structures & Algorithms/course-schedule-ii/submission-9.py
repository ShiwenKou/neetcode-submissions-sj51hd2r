class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        adjList = collections.defaultdict(list)

        for n1, n2 in prerequisites:
            adjList[n1].append(n2) # directed graph

        cycle = set() # detected loop
        seen = set() # processed node
        res = []
        def dfs(curr):

            if curr in cycle:
                return False
            if curr in seen:
                return True
            cycle.add(curr)

            for nei in adjList[curr]:
                if dfs(nei) == False: # a loop detected, recursively return back
                    return False
            # curr doesn't have a nei, so the above dfs won't run

            seen.add(curr)
            cycle.remove(curr)
            res.append(curr)
            return True
        
        for node in range(numCourses):
            if dfs(node) == False:
                return []
        return res