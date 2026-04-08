class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]
        
        memo = {1: nums[0], 2: max(nums[0], nums[1])}

        # f(i) = max(nums[i-1]+)

        # 2, 9, 8, 3, 6

        # f(1) = 2
        # f(2) = 9
        # f(3) = 10 = nums[3-1] + f(1)
        # f(4) = max(f(i - 1), f(i-2) + nums[i -1]) = 12
        # f(5) = f(3) + nums[5-1] = 16


        def helper(i):
            if i in memo:
                return memo[i]
            else:
                memo[i] = max(helper(i - 1), helper(i - 2) + nums[i - 1])
                return memo[i]
        return helper(len(nums))