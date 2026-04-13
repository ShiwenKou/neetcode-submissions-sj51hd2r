class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]


        def helper(lst):
            memo = {}
            def dfs(i):
                if i >= len(lst):
                    return 0
                if i in memo:
                    return memo[i]

                res = max(dfs(i + 2) + lst[i], dfs(i + 1))
                memo[i] = res
                return res
            
            return dfs(0)

        return max(helper(nums[:-1]), helper(nums[1:]))
