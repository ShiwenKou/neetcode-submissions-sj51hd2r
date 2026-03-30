class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        res = []
        sol = []
        nums.sort()


        def dfs(i):
            if i >= len(nums):
                res.append(sol[:])
                return

            sol.append(nums[i])
            dfs(i+1)

            sol.pop()
            
            while i + 1 < len(nums) and nums[i + 1] == nums[i]:
                i += 1
            dfs(i + 1)
        dfs(0)
        return res