class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        return max(nums, key= nums.count)
        