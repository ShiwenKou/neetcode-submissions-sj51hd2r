class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        from functools import cache
        @cache
        def dfs(start):

            if start == len(nums):
                return 0

            

            res = 1
            for nxt in range(start, len(nums)):
                if nums[nxt] > nums[start]:
                    res = max(1 + dfs(nxt), res)
            return res

        return max(dfs(start) for start in range(len(nums)))