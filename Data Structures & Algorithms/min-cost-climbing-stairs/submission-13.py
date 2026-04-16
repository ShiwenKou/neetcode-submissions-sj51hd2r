class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        

        from functools import cache
        @cache
        def dfs(i):
            if i > len(cost) - 1:
                return 0

            res = 0
            
            res += min(dfs(i + 1) + cost[i], dfs(i + 2) + cost[i]) 
            return res
        
        return min(dfs(0), dfs(1))