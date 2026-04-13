class Solution:
    def canJump(self, nums: List[int]) -> bool:
        sys.setrecursionlimit(9999)
        from functools import cache
        @cache
        def dfs(i):

            if i >= len(nums) - 1:
                return True

            for j in range(1, nums[i] + 1):

                if dfs(i + j):
                    return True
            
            return False
        return dfs(0)