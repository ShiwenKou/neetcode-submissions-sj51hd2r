class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxx, minn = 1, 1
        res = nums[0]
        for n in nums:

            maxx, minn = max(maxx * n, minn * n, n), min(maxx * n, minn * n, n)
            res = max(res, maxx)
        return res