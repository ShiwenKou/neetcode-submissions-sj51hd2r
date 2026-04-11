class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]

        def helper(lst):
            if len(lst) == 1:
                return lst[0]
            memo = {}
            def dfs(i):
                if i >= len(lst):
                    return 0
                if i in memo:
                    return memo[i]
                res = 0
                res += max(dfs(i + 2) + lst[i], dfs(i + 1))
                memo[i] = res
                return res
            return dfs(0)
        return max(helper(nums[1:]), helper(nums[:-1]))