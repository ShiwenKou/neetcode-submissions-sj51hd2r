class Solution:
    def climbStairs(self, n: int) -> int:
        

        memo = {1:1, 2:2}

        def helper(i):
            if i in memo:
                return memo[i]
            else:
                memo[i] = helper(i - 2) + helper(i - 1)
                return memo[i]
        return helper(n)