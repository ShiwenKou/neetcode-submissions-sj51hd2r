class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adj = collections.defaultdict(list)

        for crs, pre in prerequisites:
            adj[crs].append(pre)

        seen = set()
        def dfs(crs):
            if adj[crs] == []:
                return True
            if crs in seen:
                return False
            
            seen.add(crs)

            for pre in adj[crs]:
                if dfs(pre) == False: return False

            seen.remove(crs)
            adj[crs] = []
            return True
        
        for crs in range(numCourses):
            if dfs(crs) == False: return False
        return True