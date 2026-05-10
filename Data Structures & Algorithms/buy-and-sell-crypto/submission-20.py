class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        

        left = 0
        maxPrice = 0

        for right in range(len(prices)):

            maxPrice = max(maxPrice, prices[right] - prices[left])

            if prices[right] < prices[left]:
                left = right

        return maxPrice