class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        if not nums:
            return [[]]
        
        nums.sort()  # sort so duplicates are adjacent
        perms = self.permuteUnique(nums[1:])

        for p in perms:
            for i in range(len(p) + 1):
                p_copy = p.copy()
                p_copy.insert(i, nums[0])
                res.append(p_copy)

                # if we just placed nums[0] before an identical value, stop
                if i < len(p) and p[i] == nums[0]:
                    break
        return res