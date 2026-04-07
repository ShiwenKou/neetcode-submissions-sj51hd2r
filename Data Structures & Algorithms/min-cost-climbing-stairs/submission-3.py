class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        # i = 1 cost = 0
        # i = 2 cost = 0 or 1
        # i = 3 cost = 3 or 2
        # i = 4 cost = min(i=2) + 2 = 2 or min(i=3) + 3 = 5

        memo = {0:0, 1:0}

        # f(i) = min(helper(i - 2) + cost[i]; helper(i - 1))

        def helper(i):

            if i in memo:
                return memo[i]
            else:
                memo[i] = min(helper(i - 2) + cost[i - 2], helper(i - 1) + cost[i - 1])
                return memo[i]
        return helper(len(cost))