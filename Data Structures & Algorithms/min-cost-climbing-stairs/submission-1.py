class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        memo = {0:0, 1:0}

        def get_cost(i):
            if i in memo:
                return memo[i]
            else:
                memo[i] = min(cost[i - 1] + get_cost(i - 1),
                          cost[i - 2] + get_cost(i - 2))
                return memo[i]
        return get_cost(len(cost))