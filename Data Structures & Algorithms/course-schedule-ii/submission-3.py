class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        adjList = collections.defaultdict(list)

        for crs, pre in prerequisites:
            adjList[crs].append(pre)

        seen = set()
        cycle = set()
        output = []


        def dfs(crs):
            if crs in cycle:
                return False
            if crs in seen:
                return True
            cycle.add(crs)

            for pre in adjList[crs]:
                if dfs(pre) == False: return False
            
            seen.add(crs)
            output.append(crs)
            cycle.remove(crs)

            return True
        
        for crs in range(numCourses):
            if dfs(crs) == False: return []
        return output
        