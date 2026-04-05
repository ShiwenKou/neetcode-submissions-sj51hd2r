class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]
        
        return max(self.helper(nums[1:]), self.helper(nums[:len(nums) - 1]))
    def helper(self, lst):
        if len(lst) == 1:
            return lst[0]
        memo = {0:lst[0], 1:max(lst[0], lst[1])}

        def calc_money(i):
            if i in memo:
                return memo[i]
            else:
                memo[i] = max(calc_money(i - 2) + lst[i], calc_money(i - 1))
                return memo[i]
        return calc_money(len(lst) - 1)