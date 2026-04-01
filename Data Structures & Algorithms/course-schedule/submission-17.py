class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adjList = collections.defaultdict(list)

        for crs, pre in prerequisites:
            adjList[crs].append(pre)

        seen = set()
        cycle = set()

        def dfs(crs):
            if crs in cycle:
                return False
            if crs in seen:
                return True
            cycle.add(crs)
            for pre in adjList[crs]:
                if dfs(pre) == False: return False
            
            cycle.remove(crs)
            seen.add(crs)
            return True
#1->2       
        for crs in range(numCourses):
            if dfs(crs) == False: return False
        return True