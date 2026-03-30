class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        start = 0
        end = 0
        idx = 0
        while start < len(nums):

            if end < len(nums) and nums[start] == nums[end]:
                end += 1
            else:
                nums[idx] = nums[start]
                start = end
                idx += 1
                if end < len(nums): end += 1
        
        return idx