class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        # make negative and 0 to len(nums) + 2
        # make number within 1-len(nums) to negative

        # check pos/negative

        for i in range(len(nums)):
            if nums[i] <=0 :
                nums[i] = len(nums) + 2
        for i in range(len(nums)):

            if abs(nums[i]) <= len(nums) and abs(nums[i]) >= 1:
                index = abs(nums[i]) -1
                nums[index] = abs(nums[index]) * -1
        
        for i in range(len(nums)):
            if nums[i] > 0:
                return i +1
        return len(nums) +1

        