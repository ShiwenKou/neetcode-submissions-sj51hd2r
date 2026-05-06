class Solution:
    def canJump(self, nums: List[int]) -> bool:
        sys.setrecursionlimit(20000)
        from functools import cache

        @cache
        def dfs(i):
            if i >= len(nums) - 1:
                return True

            res = False
            
            for j in range(1, nums[i] + 1):

                res = dfs(i + j) or res

            
            return res

        return dfs(0)