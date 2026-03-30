class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i] <= 0:
                nums[i] = len(nums)+2

        for i in range(len(nums)):
            candidate = abs(nums[i]) - 1

            if candidate >= 0 and candidate < len(nums):
                nums[candidate]= -abs(nums[candidate])
        for i in range(1, len(nums)+1):
            if nums[i-1] > 0:
                return i
        return len(nums) + 1

        


        