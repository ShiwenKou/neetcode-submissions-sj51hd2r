class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        

        # if we have stock. we have two options to sell or to skip

        # if we don't have stock, either we buy or we skip
        memo = {}
        def dfs(i, stock):

            if i >= len(prices):
                return 0
            
            if (i, stock) in memo:
                return memo[(i, stock)]
            if stock:

                res = max(dfs(i + 2, False) + prices[i], dfs(i + 1, True))

            else:
                res = max(-prices[i] + dfs(i + 1, True), dfs(i + 1, False))
            memo[(i, stock)] = res
            return res

        return dfs(0, False)



