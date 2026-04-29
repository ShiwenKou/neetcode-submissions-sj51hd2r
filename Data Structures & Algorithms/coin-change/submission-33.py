class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        from functools import cache
        @cache
        def dfs(remaining):

            if remaining == 0:
                return 0

            if remaining < 0:
                return float('inf')
            best = float('inf')
            for n in coins:

                best = min(best, 1 + dfs(remaining - n))

            return best

        ans = dfs(amount)
        return ans if ans != float('inf') else -1