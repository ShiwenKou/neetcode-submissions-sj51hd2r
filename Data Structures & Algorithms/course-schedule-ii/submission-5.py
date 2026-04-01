class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjList = collections.defaultdict(list)
        for crs, pre in prerequisites:
            adjList[crs].append(pre)

        cycle = set()
        seen = set()
        res = []
        sol = []
        def dfs(crs):
            if crs in cycle:
                return False
            if crs in seen:
                return True

            cycle.add(crs)
            for pre in adjList[crs]:
                if dfs(pre) == False : return False

            cycle.remove(crs)
            seen.add(crs)
            res.append(crs)
            return True
        

        for crs in range(numCourses):

            if crs not in seen:
                if dfs(crs) == False: return []
        return res