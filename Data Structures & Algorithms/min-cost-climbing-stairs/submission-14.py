class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        from functools import cache
        @cache
        def dfs(i):

            if i >= len(cost):
                return 0

            

            res = cost[i] + min(dfs(i + 1), dfs(i + 2))

            return res
        
        return min(dfs(0), dfs(1))