class Solution:
    def climbStairs(self, n: int) -> int:
        
        memo = {}
        def dfs(remaining):
            if remaining == 0:
                return 1
            if remaining < 0:
                return 0
            
            if  remaining in memo:
                return memo[remaining]
            
            res = 0

            res += dfs(remaining - 1) + dfs(remaining - 2)
            memo[remaining] =res
            return res

        return dfs(n)