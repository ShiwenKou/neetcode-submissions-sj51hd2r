class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        res = []

        adjList = collections.defaultdict(list)
        for n1, n2 in prerequisites:
            adjList[n1].append(n2)
        

        cycle = set()
        seen = set()

        def dfs(node):
            if node in cycle: # visiting
                return False
            
            if node in seen: # visited
                return True
            
            cycle.add(node)

            for nei in adjList[node]:

                if dfs(nei) == False:
                    return False # whenever there exists a loop we return []
        
            # when curr node has no nei, we backtracking

            res.append(node)
            seen.add(node)
            cycle.remove(node)

        for crs in range(numCourses):
            if dfs(crs) == False:
                return []
        return res