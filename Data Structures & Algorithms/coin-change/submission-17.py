class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        

        sys.setrecursionlimit(100000)
        memo = {}
        def dfs(i, remaining):
            if remaining == 0:
                return 0
            if i >= len(coins) or remaining < 0:
                return float('inf')
            if (i, remaining) in memo:
                return memo[(i, remaining)]

            res = min(1 + dfs(i, remaining - coins[i]), dfs(i + 1, remaining))
            memo[(i, remaining)] = res
            return res

        res = dfs(0, amount) 
        if res == float('inf'): return -1
        else: return res
