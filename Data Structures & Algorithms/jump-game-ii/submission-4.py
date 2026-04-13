class Solution:
    def jump(self, nums: List[int]) -> int:
        
        sys.setrecursionlimit(99999)
        from functools import cache
        @cache
        def dfs(i):
            if i >= len(nums):
                return float('inf')
            if i == len(nums) - 1:
                return 0

            res = float('inf')

            for j in range(1 , nums[i] + 1):

                res = min(1 + dfs(i + j), res)
            
            return res

        return dfs(0)
