class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        maxx, minn = 1, 1
        res = nums[0]
        for n in nums:

            maxx, minn = max(n * maxx, n * minn, n), min(n * maxx, n * minn, n)
            res = max(maxx, res)
        return res