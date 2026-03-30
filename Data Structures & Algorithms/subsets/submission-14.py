class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        res = []
        subset = []
    
        def dfs(i):
            if i >= len(nums):
                # basecase
                res.append(subset[:])
                return

            subset.append(nums[i])
            # include
            dfs(i+1)
            subset.pop()
            # not include
            dfs(i+1)

        dfs(0)
        return res
        