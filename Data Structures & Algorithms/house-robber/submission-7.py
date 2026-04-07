class Solution:
    def rob(self, nums: List[int]) -> int:
        
        # i = 0 , ans = 1
        # i = 1, ans = max(2, 2 - 1) = 1

        # i = 2, ans = max(f(i-1), i-2)

        # i = max(f(i - 2) + nums(i - 1), f(i - 1) )

        if len(nums) == 1:
            return nums[0]
       
        memo = {0: nums[0], 1: max(nums[0], nums[1])}

        def helper(i):
            if i in memo:
                return memo[i]
            else:
                memo[i] = max(helper(i - 2) + nums[i], helper(i - 1))
                return memo[i]
        return helper(len(nums) - 1)

        # f(0) = 2
        # f(1) = 9
        # f(2) = 10 = (f(i-2) + nums[i], f(i-1)) = max(10, 9) = 10
        # f(3) = max(f(1) + nums[i], f(2)) = max(9+3,10) = 12
        # f(4) = max(f(2) + nums[3], f(3)) = max(10+6, 12)
