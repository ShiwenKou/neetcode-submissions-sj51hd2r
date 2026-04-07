class Solution:
    def climbStairs(self, n: int) -> int:
        
        # n = 1 climb one way
        # n = 2 climb two ways [1,1] [2]
        # n = 3 climb [1,1,1][1,2][2,1] 3 ways

        # n = 4 climb [1,1,1,1],[1,2,1],[2,1,1],[2,1,1],[2,2]

        # f(i) = f(i -2) + f(i -1)

        memo = {1:1, 2:2}

        def helper(i):
            if i in memo:
                return memo[i]
            else:
                memo[i] = helper(i - 2) + helper(i - 1)
                return memo[i]
        
        return helper(n)