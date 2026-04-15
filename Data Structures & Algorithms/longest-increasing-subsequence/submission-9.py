class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sys.setrecursionlimit(9999)
        from functools import cache
        @cache
        def dfs(i, prev):
            if i == len(nums):
                return 0

            
            if nums[i] > prev: # only if current nums[i] > nums[i - 1] 我们才有选择
                res = max(1 + dfs(i + 1, nums[i]), dfs(i + 1, prev)) # 选或者不选
            
            else:
                res = dfs(i + 1, prev) # 不选

            return res

        
        return dfs(0, float('-inf'))
        