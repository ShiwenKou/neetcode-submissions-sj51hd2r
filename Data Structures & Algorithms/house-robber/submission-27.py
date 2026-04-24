class Solution:
    def rob(self, nums: List[int]) -> int:
        
        from functools import cache
        @cache
        def dfs(i):
            if i >= len(nums):
                return 0


            res = max(dfs(i + 1), dfs(i + 2) + nums[i])

            return res

        return dfs(0)