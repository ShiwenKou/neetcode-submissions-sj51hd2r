class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        summ = sum(nums)

        summ2 = sum(range(len(nums) + 1))

        return summ2 - summ