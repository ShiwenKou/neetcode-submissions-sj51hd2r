class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def solver(lst):
            if len(lst) == 1:
                return lst[0]
            memo = {0:lst[0], 1: max(lst[0], lst[1])}
            def helper(i):
                if i in memo:
                    return memo[i]
                else:
                    memo[i] = max(helper(i - 2) + lst[i], helper(i - 1))
                    return memo[i]
            return helper(len(lst) - 1)
        if len(nums) == 1:
            return nums[0]

        res1 = solver(nums[:-1])
        res2 = solver(nums[1:])
        return max(res1, res2)