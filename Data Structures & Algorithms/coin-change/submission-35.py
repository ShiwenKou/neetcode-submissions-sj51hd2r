class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        # memoization
        from functools import cache
        @cache
        def dfs(remaining):

            if remaining == 0:
                return 0
            if remaining < 0:
                return float('inf')


            res = float('inf')
            for n in coins:

                res = min(res, 1 + dfs(remaining - n))

            return res

        
        ans = dfs(amount)

        return -1 if ans == float('inf') else ans

        