class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        expect_sum = sum(range(len(nums) + 1))

        real_sum = sum(nums)
        return expect_sum - real_sum