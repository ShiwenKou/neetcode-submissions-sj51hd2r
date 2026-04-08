class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # a loop detected return []

        # seen set

        adjList = collections.defaultdict(list)
        for n1, n2 in prerequisites:
            adjList[n1].append(n2)

        res = []
        seen = set()
        cycle = set()


        def dfs(crs):
            if crs in cycle:
                return False
            if crs in seen:
                return True
            cycle.add(crs)


            for nei in adjList[crs]:
                if dfs(nei) == False:
                    return False
            
            cycle.remove(crs)
            seen.add(crs)
            res.append(crs)
            return True


        for crs in range(numCourses):
            if dfs(crs) == False:
                return []
        
        return res