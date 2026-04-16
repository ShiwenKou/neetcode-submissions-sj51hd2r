class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        from functools import cache
        sys.setrecursionlimit(9999)
        @cache
        def dfs(i, prev):

            if i == len(nums):
                return 0

            
            if nums[i] > prev:
                # we choose or not
                res = max(1 + dfs(i + 1, nums[i]), dfs(i + 1, prev))
            else:
                # skip only index i
                res = dfs(i + 1, prev)

            return res

        return dfs(0, float('-inf'))