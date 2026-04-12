class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        
        memo = {}
        def dfs(i):

            
            if i >= len(cost):
                return 0
            if i in memo:
                return memo[i]

            
            res = min(dfs(i + 2) + cost[i], dfs(i + 1) + cost[i])

            # 原理就是。我有两个选择， 付钱之后走一步或两步。看那个能在付钱最少的前提下让i>=len(cost)
            memo[i] = res
            return res

        return min(dfs(0), dfs(1))