class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # so normally we can just iterate twice the prices. to find prices[i] - prices[j]

        # and we know we can only use prices[i] - prices[j] j > i.

        # so we can take advantage of that by using two pointers.

        left = right = 0
        res = 0
        for right in range(len(prices)):
            res = max((prices[right] - prices[left]), res)

            if prices[right] < prices[left]:
                left = right

        return res





        