class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        minn, maxx = 1 , 1
        res = float('-inf')
        for num in nums:
            # if num == 0:
            #     minn, maxx = 1, 1
            #     continue
            
            minn, maxx = min(num * minn, num * maxx, num), max(num * minn, num * maxx, num)
            res = max(res, maxx)
    
        return res