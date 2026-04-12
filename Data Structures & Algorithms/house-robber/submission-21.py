class Solution:
    def rob(self, nums: List[int]) -> int:
        
        memo = {}
        def dfs(i):
            if i in memo:
                return memo[i]
            if i >= len(nums):
                return 0

            res = max(dfs(i + 2) + nums[i], dfs(i + 1))
            memo[i] = res
            return res

        return max(dfs(0), dfs(1))