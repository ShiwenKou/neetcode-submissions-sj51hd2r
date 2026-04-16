class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        minn, maxx = 1, 1
        res = float('-inf')
        for n in nums:

            minn, maxx = min(minn * n, maxx * n, n), max(minn * n, maxx * n, n)
            res = max(res, maxx)
        return res



