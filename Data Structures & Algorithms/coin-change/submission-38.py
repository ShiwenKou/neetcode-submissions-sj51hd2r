class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        

        from functools import cache
        @cache
        def dfs(remaining):

            if remaining == 0:
                return 0
            if remaining < 0:
                return float('inf')
            

            return min(1 + dfs(remaining - n) for n in coins)
        ans = dfs(amount)
        return ans if ans != float('inf') else -1

            