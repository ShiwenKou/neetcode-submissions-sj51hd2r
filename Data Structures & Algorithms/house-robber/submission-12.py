class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        memo = {0:nums[0], 1: max(nums[0], nums[1])}

        # f(2) = f(i - 2) + nums[i], f(i - 1)

        def helper(i):

            if i in memo:
                return memo[i]

            else:
                memo[i] = max(helper(i - 2) + nums[i], helper(i - 1))
                return memo[i]
        
        return helper(len(nums) - 1)