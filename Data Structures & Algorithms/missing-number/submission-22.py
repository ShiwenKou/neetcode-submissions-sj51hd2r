class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        n = len(nums)

        expected_sum = n * (n + 1) // 2

        real_sum = sum(nums)
        return expected_sum - real_sum