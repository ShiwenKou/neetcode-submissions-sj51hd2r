class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        

        left = 0

        res = 0
        for right in range(len(prices)):


            res = max(res, prices[right] - prices[left])

            if prices[right] < prices[left]:
                left = right

        return res