class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        solution = []
        res = []

        def dfs(i, solution, total):

            if i < len(nums) and total == target:
                res.append(solution[:])
                return
            
            if i >= len(nums) or total > target:
                return
            solution.append(nums[i])
            dfs(i, solution, total + nums[i])
            solution.pop()
            dfs(i + 1, solution, total)
        
        dfs(0, [], 0)
        return res