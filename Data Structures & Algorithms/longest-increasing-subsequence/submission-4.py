class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        

        from functools import cache
        @cache
        def dfs(start):


            best = 1
            for nxt in range(start, len(nums)):
                if nums[nxt] > nums[start]:
                    best = max(best, 1 + dfs(nxt))

            return best
        
        return max(dfs(start) for start in range(len(nums)))

