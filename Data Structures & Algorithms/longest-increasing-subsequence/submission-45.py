class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sys.setrecursionlimit(9999)
        from functools import cache
        @cache
        def dfs(i, prev):
            if i == len(nums):
                return 0

            

            if nums[i] > prev:
                # take or not

                res = max(1 + dfs(i + 1, nums[i]), dfs(i + 1, prev))
            
            else:
                # no take
                res = dfs(i + 1, prev)
            return res
        
        return dfs(0, float('-inf'))