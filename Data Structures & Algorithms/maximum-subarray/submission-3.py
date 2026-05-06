class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        res = float('-inf')

        cur = 0


        for n in nums:
            if cur < 0:
                cur = 0

            cur = n + cur

            res = max(cur, res)
        return res