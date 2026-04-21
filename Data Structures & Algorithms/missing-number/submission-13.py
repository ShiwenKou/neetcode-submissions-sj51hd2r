class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        for i in range(len(nums)):
            nums[i] = nums[i] + 1


        for i in range(len(nums)):
            val = abs(nums[i])
            if val <= len(nums):
                idx = val - 1
                nums[idx] = abs(nums[idx]) * -1

        for i in range(len(nums)):

            if nums[i] > 0:
                return i
        return len(nums)