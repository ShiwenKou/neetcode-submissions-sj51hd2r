class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        expected_sum = n * (n + 1) // 2

        cur_sum = sum(nums)

        return expected_sum - cur_sum