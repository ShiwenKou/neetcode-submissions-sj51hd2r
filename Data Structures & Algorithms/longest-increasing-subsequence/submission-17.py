class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        from functools import cache
        @cache
        def dfs(i):

            if i == len(nums):
                return 0
            best = 1
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    best = max(best, 1 + dfs(j))
            return best


        return max(dfs(start) for start in range(len(nums)))