class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # this is a directed graph. need two sets
        adjList = collections.defaultdict(list)
        for n1, n2 in prerequisites:
            adjList[n1].append(n2)
        
        cycle = set() # detecting loops down the current path
        seen = set() # checked node

        def dfs(curr):
            if curr in cycle:
                return False
            if curr in seen:
                return True
            
            cycle.add(curr)

            for nei in adjList[curr]:
                if dfs(nei) == False:
                    return False # a loop detected, recursively return False
            
            cycle.remove(curr) # we are backtracking the path. in case two courses have the same prerequisite
            seen.add(curr) # this curr has been checked
            return True
        
        for node in range(numCourses):
            if dfs(node) == False:
                return False
        return True
                    
