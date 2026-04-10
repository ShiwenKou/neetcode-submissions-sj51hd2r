class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        


        # 1-> holding
        # 0 -> no holding
        memo = {}
        def dfs(i, holding): # true == sell
            if i >= len(prices):
                return 0
            if (i, holding) in memo:
                return memo[(i, holding)]

            reset = dfs(i + 1, holding) # cooldown

            if holding:
                action = prices[i] + dfs(i + 2, 0) # sell
            else:
                action = -prices[i] + dfs(i + 1, 1)

            res = max(reset, action)
            memo[(i, holding)] = res
            return res 

        return dfs(0, 0)
                
