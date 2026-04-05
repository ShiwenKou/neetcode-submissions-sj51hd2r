class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        memo = {0:0, 1:0}
        n = len(cost)
        def min_cost(i):
            if i in memo:
                return memo[i]
            
            else:
                memo[i] = min(cost[i-1]+ min_cost(i-1),
                              cost[i-2]+min_cost(i-2))
                return memo[i]
        return min_cost(n)