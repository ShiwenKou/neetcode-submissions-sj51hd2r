class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []


        def dfs(i, sol, total):

            if total == target:
                res.append(sol[:])
                return
            if i >= len(nums) or total > target:
                return
            

            sol.append(nums[i])

            dfs(i, sol, total + nums[i])

            sol.pop()
            dfs(i+1, sol, total)

        dfs(0, [], 0)
        return res