class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}
        def dfs(i, remaining):
            if remaining == 0:
                return 1
            if (i, remaining) in memo:
                return memo[(i, remaining)]
            
            res = 0
            for j in range(i, len(coins)):       # 枚举"下一枚用 coins[j]"
                if remaining >= coins[j]:
                    res += dfs(j, remaining - coins[j])  # 注意传 j,不是 j+1
            
            memo[(i, remaining)] = res
            return res

        return dfs(0, amount)