class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjList = collections.defaultdict(list)
        for n1, n2 in prerequisites:
            adjList[n1].append(n2)
        
        cycle = set()
        seen = set()
        res = []
        def dfs(crs):

            if crs in cycle:
                return False
            if crs in seen:
                return True

            cycle.add(crs)
            for nei in adjList[crs]:
                if dfs(nei) == False:
                    return False

            seen.add(crs)
            res.append(crs)
            cycle.remove(crs)
            return True
        
        for crs in range(numCourses):
            if dfs(crs) == False:
                return []

        return res


