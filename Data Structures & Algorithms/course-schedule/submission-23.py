class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        # directed graph. will return False, if there is a loop.

        cycle = set() # visiting
        seen = set() # visited

        adjList = collections.defaultdict(list)
        for n1, n2 in prerequisites:
            adjList[n1].append(n2)

        def dfs(node):
            if node in cycle:
                return False
            if node in seen:
                return True
            
            cycle.add(node)

            for nei in adjList[node]:
                if dfs(nei) == False: # a loop detected
                    return False
            
            cycle.discard(node)
            seen.add(node)
            return True

        for node in range(numCourses):
            if not dfs(node):
                return False
        return True