class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        adjList = collections.defaultdict(list)

        for crs, pre in prerequisites:
            adjList[crs].append(pre)
        
        cycle = set()
        seen = set()
        output = []

        def dfs(crs):
            if crs in cycle:
                return False
            if crs in seen:
                return True
            
            cycle.add(crs)

            for pre in adjList[crs]:
                if dfs(pre) == False:
                    return False
            
            seen.add(crs)
            cycle.remove(crs)
            output.append(crs)
            return True
        
        for pre in range(numCourses):
            if dfs(pre) == False:
                return []
        return output