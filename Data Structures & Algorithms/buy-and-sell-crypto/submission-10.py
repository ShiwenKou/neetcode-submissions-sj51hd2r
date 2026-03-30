class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        left, right = 0, 0
        maxRes = 0
        for right in range(len(prices)):

            res = prices[right] - prices[left]
            maxRes = max(res, maxRes)

            if prices[right] < prices[left]:
                left = right

        return maxRes
        