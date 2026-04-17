class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        from functools import cache
        summ = sum(nums)
        if summ % 2:
            return False
        
        target = summ // 2        
        @cache
        def dfs(i, remaining):
            if remaining == 0:
                return True
            
            if i >= len(nums) or remaining < 0:
                return False
            

            res = dfs(i + 1, remaining - nums[i]) or dfs(i + 1, remaining)

            return res
        
        return dfs(0, target)