class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        res = []
        if len(nums) == 1: # we hit the base case here
            return [nums[:]] # return the base case

        for _ in range(len(nums)):

            n = nums.pop(0)

            perms = self.permute(nums) # [2,3] [3,2]

            for perm in perms:
                perm.append(n)
            res.extend(perms)

            nums.append(n)
        return res
        