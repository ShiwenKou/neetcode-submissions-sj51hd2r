class Solution:
    def rob(self, nums: List[int]) -> int:
        from functools import cache

        if len(nums) == 1:
            return nums[0]


        
        def helper(lst):

            @cache
            def dfs(i):

                if i >= len(lst):
                    return 0

                res = max(dfs(i + 2) + lst[i], dfs(i + 1))
                return res

            return dfs(0)

        return max(helper(nums[:-1]), helper(nums[1:]))