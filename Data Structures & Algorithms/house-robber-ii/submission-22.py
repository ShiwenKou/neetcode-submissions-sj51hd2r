class Solution:
    def rob(self, nums: List[int]) -> int:
        
        # from functools import cache
        # @cache
        if len(nums) == 1:
            return nums[0]
        def helper(lst):
            from functools import cache
            @cache
            def dfs(i):
                if i >= len(lst):
                    return 0

                res = max(dfs(i + 1), lst[i] + dfs(i + 2))

                return res
            
            return dfs(0)
    

        return max(helper(nums[:-1]), helper(nums[1:]))