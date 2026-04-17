class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        from functools import cache
        @cache
        def dfs(i, remaining):
            if remaining == 0:
                return 0
            if i >= len(coins) or remaining < 0:
                return float('inf')


            res = min(1 + dfs(i, remaining - coins[i]), dfs(i + 1, remaining))
            return res

        
        ans = dfs(0, amount)
        if ans == float('inf'):
            return - 1
        else:
            return ans