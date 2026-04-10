class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        memo = {}
        def dfs(i, remaining):
            if  i == len(nums) and remaining == 0:
                return 1
            if i >= len(nums):
                return 0
            if (i, remaining) in memo:
                return memo[(i, remaining)]
            
            res = 0
            res += dfs(i + 1, remaining + nums[i]) + dfs(i + 1, remaining - nums[i])
            
            memo[(i, remaining)] = res
            return res

        return dfs(0, target)