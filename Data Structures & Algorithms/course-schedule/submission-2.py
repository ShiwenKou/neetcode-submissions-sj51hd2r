class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        mappings = collections.defaultdict(list)
        for crs, pre in prerequisites:
            mappings[crs].append(pre)
        seen = set()
        def dfs(crs):
            if mappings[crs] == []:
                return True
            if crs in seen:
                return False
            seen.add(crs)
            for pre in mappings[crs]:
               if dfs(pre) == False: return False
            
            seen.remove(crs)
            mappings[crs] = []

            return True
        
        for crs in range(numCourses):
            if dfs(crs) == False: return False
        return True
        