class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        

        memo = {}
        def dfs(i):

            if i >= len(cost):
                return 0
            
            if i in memo:
                return memo[i]

            res = 0
            res += min(dfs(i + 1) + cost[i], dfs(i + 2) + cost[i])
            memo[i] = res
            return res

        
        return min(dfs(0), dfs(1))