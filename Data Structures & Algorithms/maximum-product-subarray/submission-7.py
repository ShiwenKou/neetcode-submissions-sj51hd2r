class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        res = max(nums)
        maxx, minn = 1, 1

        for n in nums:
            if n == 0:
                maxx, minn = 1, 1
                continue
            
            maxx, minn = max(n * maxx, n * minn, n), min(n * maxx, n * minn, n)

            res = max(maxx, res)
        return res