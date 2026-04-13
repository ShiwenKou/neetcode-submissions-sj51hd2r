class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        sys.setrecursionlimit(999999)
        memo = {}
        def dfs(remaining):

            if remaining == 0:
                return 0
            
            if remaining < 0:
                return float('inf')
            
            if remaining in memo:
                return memo[remaining]

            res = float('inf')
            for coin in coins:
                res = min(res, 1 + dfs(remaining - coin))
            memo[remaining] = res
            return res
        
        ans = dfs(amount)
        if ans == float('inf'):
            return -1
        else:
            return ans
