class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        

        res = []
        sol = []

        def dfs(i, remaining):

            if remaining == 0:
                res.append(sol[:])
                return

            if i >= len(nums) or remaining < 0:
                return

            

            sol.append(nums[i])
            dfs(i, remaining - nums[i])
            sol.pop()
            dfs(i + 1, remaining)

        
        dfs(0, target)
        return res