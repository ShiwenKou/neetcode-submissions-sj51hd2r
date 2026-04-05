class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        n = len(cost)
        memo = {0:0, 1:0}
        def helper(i):
            if i in memo:
                return memo[i]
            else:
                memo[i] = min(helper(i - 1) + cost[i - 1], helper(i - 2) + cost[i - 2])
                return memo[i]
        return helper(n)