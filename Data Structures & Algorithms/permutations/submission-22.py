class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        seen = set()

        res = []
        sol = []
        def dfs():

            if len(sol) == len(nums):
                res.append(sol[:])
                return

            for i in range(len(nums)):

                if nums[i] not in seen:
                    seen.add(nums[i])
                    sol.append(nums[i])

                    dfs()

                    seen.remove(nums[i])
                    sol.pop()

        dfs()
        return res

        