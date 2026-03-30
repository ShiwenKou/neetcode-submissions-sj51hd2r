class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        res = []
        sol = []

        def dfs(i):
            if i == len(nums):
                res.append(sol[:])
                return
            
            sol.append(nums[i])

            dfs(i + 1)

            sol.pop()
            dfs(i + 1)

        dfs(0)
        return res
# O(n*2^n) where n is the length of nums
# O(n) n frame recursive calls
        