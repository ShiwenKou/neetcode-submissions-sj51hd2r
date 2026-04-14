class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        from functools import cache
        sys.setrecursionlimit(99999)

        @cache
        def dfs(remaining):

            if remaining == 0:
                return 0
            if remaining < 0:
                return float('inf')
            
            res = float('inf')
            for n in coins:

                res = min(1 + dfs(remaining - n), res)

            return res
        ans = dfs(amount)
        return -1 if ans == float('inf') else ans