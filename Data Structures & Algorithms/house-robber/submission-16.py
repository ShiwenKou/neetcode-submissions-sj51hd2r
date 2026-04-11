class Solution:
    def rob(self, nums: List[int]) -> int:
        from functools import cache
        @cache
        def dfs(i, total):

            if i >= len(nums):
                return total


            res = max(dfs(i + 2, total + nums[i]), dfs(i + 1, total))
            return res

        return dfs(0, 0)
