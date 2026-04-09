class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        from functools import cache

        if sum(nums) % 2:
            return False
        target = sum(nums) / 2
        @cache
        def dfs(i, total):

            if total == target:
                return True
            
            if i >= len(nums) or total > target:
                return False
            

            res = dfs(i + 1, total + nums[i]) or dfs(i + 1, total)

            return res

        return dfs(0, 0)