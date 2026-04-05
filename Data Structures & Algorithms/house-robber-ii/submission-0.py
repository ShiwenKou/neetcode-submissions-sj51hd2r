class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]
        return max(self.helper(nums[:-1]), self.helper(nums[1:]))

    def helper(self, lst):
        if len(lst) == 1:
            return lst[0]
        memo = {0:lst[0], 1:max(lst[0], lst[1])}
        
        def calc_cost(i):
            if i in memo:
                return memo[i]
            else:
                memo[i] = max(calc_cost(i - 2) + lst[i], calc_cost(i - 1))
                return memo[i]
        return calc_cost(len(lst) - 1)



        