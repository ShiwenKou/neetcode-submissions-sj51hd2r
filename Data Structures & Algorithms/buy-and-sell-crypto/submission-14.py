class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        left, right = 0, 0

        res = 0

        for right in range(len(prices)):
            p = prices[right] - prices[left]
            res = max(res, p)

            if prices[right] < prices[left]: # right pointer all greater than the left one. so the best profit has alr marked in res
                left = right
        return res