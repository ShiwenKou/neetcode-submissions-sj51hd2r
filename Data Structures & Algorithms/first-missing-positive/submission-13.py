class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        for i in range(len(nums)):
            if nums[i] <= 0:
                nums[i] = len(nums) + 2
        for i in range(len(nums)):
            if 0 <= abs(nums[i]) <= len(nums):
                index = abs(nums[i]) - 1
                nums[index] = abs(nums[index]) * - 1
        for i in range(len(nums)):
            if nums[i] > 0:
                return i + 1
        return len(nums) + 1
        