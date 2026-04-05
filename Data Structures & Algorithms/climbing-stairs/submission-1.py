class Solution:
    def climbStairs(self, n: int) -> int:

       
        memo = {1:1, 2:2}

        def helper(i):
            if i in memo:
                return memo[i]
            else:
                memo[i] = helper(i - 1) + helper(i - 2)
                return memo[i]
        return helper(n)
