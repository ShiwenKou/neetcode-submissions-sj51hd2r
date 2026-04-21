class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        for i in range(len(nums)):
            nums[i] = nums[i] + 1
        
        for i in range(len(nums)):

            val = abs(nums[i])
            # we can hex from 1 to n
            if val <= len(nums):
                idx = val - 1
                nums[idx] = -abs(nums[idx])
        
        for i in range(len(nums)):
            if nums[i] > 0:
                return i - 1 + 1

        return len(nums)
