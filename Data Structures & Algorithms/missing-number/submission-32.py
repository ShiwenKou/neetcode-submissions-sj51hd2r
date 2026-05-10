class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        for i in range(len(nums)):
            nums[i] = nums[i] + 1

        for i in range(len(nums)):
            if 1 <= abs(nums[i]) <= len(nums):
                idx = abs(nums[i]) - 1
                nums[idx] = -abs(nums[idx])

        for i in range(len(nums)):
            if nums[i] > 0:
                return i
        return len(nums)