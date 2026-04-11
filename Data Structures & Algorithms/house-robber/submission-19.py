class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        def dfs(i):

            if i >= len(nums):
                return 0
            if i in memo:
                return memo[i]

            res = max(dfs(i + 2) + nums[i], dfs(i + 1))
            memo[i] = res
            return res

        return dfs(0)
