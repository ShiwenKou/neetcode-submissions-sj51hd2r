class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        minn, maxx = 1, 1
        res = float('-inf')
        for n in nums:

            minn, maxx = min(n * maxx, n * minn, n), max(n * maxx, n * minn, n)

            res = max(res, maxx)
        return res