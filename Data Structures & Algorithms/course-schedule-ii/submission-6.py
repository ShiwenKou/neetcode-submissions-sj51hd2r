class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        adjList = collections.defaultdict(list)

        for crs, pre in prerequisites:
            adjList[crs].append(pre)

        seen, cycle = set(), set()
        res = []
        def dfs(crs):
            # base case:
            if crs in cycle:
                return False
            if crs in seen:  # we only add this after a true is returned in the base case
                return True
            cycle.add(crs)
            for pre in adjList[crs]: # if crs has no pre, we don't call this dfs
                if dfs(pre) == False: return False
            
            cycle.remove(crs)
            res.append(crs)
            seen.add(crs)
        
        for crs in range(numCourses):
            if dfs(crs) == False: return []
        return res