class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        # f(1) = 1  exist
        # f(2) = 1  exist
        # f(3) = 2 f(1) + f(2)
        # f(4) = 2 f(2) + f(2)
        # f(5) = 1 exist
        # f(6) = 2 f(5) + f(1)
        # f(7) = 2 f(5) + f(2)
        # f(8) = 3 f(5) + f(3)
        # f(9) = 3 f(8) + f(1) | f(7) + f(2)
        # f(10) = 2 f(9) + f(1) | f(8) + f(2) | f(5) + f(5)
        # f(11) = 3 f(10) + f(1)


        dp = [float('inf')] * (amount + 1)

        dp[0] = 0

        for i in range(1, amount + 1):
            for c in coins:
                if i - c >= 0:
                    dp[i] = min(dp[i], 1 + dp[i - c])
        return dp[amount] if dp[amount] != float('inf') else -1