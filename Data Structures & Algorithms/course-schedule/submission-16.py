class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adjList = collections.defaultdict(list)

        for crs, pres in prerequisites:
            adjList[crs].append(pres)
        
        seen = set()


        def dfs(crs):
            if crs in seen:
                return False
            if adjList[crs] == []:
                return True
            seen.add(crs)
            for pre in adjList[crs]: # we need to see every node
                if dfs(pre) == False: return False
            
            seen.remove(crs) 
            adjList[crs] = [] # this node is clean, it has a node that has 0 prerequisite
            return True
        for crs in range(numCourses): # 担心有多个连通分量
            if dfs(crs) == False: return False
        return True