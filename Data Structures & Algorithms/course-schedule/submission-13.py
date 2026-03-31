class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adjList = collections.defaultdict(list)

        for crs, pre in prerequisites:
            adjList[crs].append(pre)

        seen = set()

        def dfs(crs):
            if adjList[crs] == []:
                return True
            if crs in seen:
                return False # a loop detected

            
            seen.add(crs)
            for pre in adjList[crs]:
                if dfs(pre) == False: return False

            seen.remove(crs)
            adjList[crs] = []
            return True
        
        for crs in range(numCourses):
            if dfs(crs) == False: return False
        return True
