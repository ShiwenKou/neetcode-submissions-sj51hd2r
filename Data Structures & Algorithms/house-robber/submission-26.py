class Solution:
    def rob(self, nums: List[int]) -> int:
        

        from functools import cache
        @cache
        def dfs(i):
            if i >= len(nums):
                return 0

            res = max(nums[i] + dfs(i + 2), dfs(i + 1))

            return res
        
        return dfs(0)