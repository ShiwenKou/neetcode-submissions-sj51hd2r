class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        return max(nums, key= lambda i : nums.count(i))
        