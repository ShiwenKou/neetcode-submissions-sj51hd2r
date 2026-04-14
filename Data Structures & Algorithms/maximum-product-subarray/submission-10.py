class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        maxx, minn = 1, 1
        res = float('-inf')
        for n in nums:
            # if n == 0:
            #     maxx, minn = 1, 1
            #     continue
            
            maxx, minn = max(maxx * n, minn * n, n), min(maxx * n, minn * n, n)
            res = max(res, maxx)
        
        return res