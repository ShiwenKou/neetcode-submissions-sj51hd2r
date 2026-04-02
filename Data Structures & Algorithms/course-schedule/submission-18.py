class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # prereq is a directed edge
        adjList = collections.defaultdict(list)

        for n1, n2 in prerequisites:
            adjList[n1].append(n2)
        
        cycle = set()
        seen = set()

        def dfs(crs):

            if crs in cycle:
                return False
            if crs in seen:
                return True # this node have a base case that returns true
            
            cycle.add(crs)

            for nei in adjList[crs]:
                # if nei in seen:
                #     return  # I'm a bit forget how to process this part
                # but i think i can comment the above, cuz i have a base case to check if crs in seen.
                # so maybe if i visit it's neighbor it should stil be ok.
                if dfs(nei) == False:
                    return False
            
            cycle.remove(crs)
            seen.add(crs)
            return True

        # i think this problem, we only need to check if there are any loops. component is not our concern

        for crs in range(numCourses):
            if dfs(crs) == False:
                return False
        return True
        
