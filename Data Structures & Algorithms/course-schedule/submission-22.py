class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adjList = collections.defaultdict(list)
        for n1, n2 in prerequisites:
            adjList[n1].append(n2)
        cycle = set() #visiting
        seen = set() # visited
        def dfs(node):

            if node in cycle:
                return False
            if node in seen:
                return True
            cycle.add(node)

            for nei in adjList[node]:

                if dfs(nei) == False:
                    return False
            
            cycle.remove(node) # curr node has no nei(means not prerequi)
            seen.add(node)
            return True
        for node in range(numCourses):
            if dfs(node) == False:
                return False
        return True
