class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sorted_nums = sorted(enumerate(nums), key=lambda x: x[1])

        left, right = 0, len(nums) - 1
        while left < right:
            current_sum = sorted_nums[left][1] + sorted_nums[right][1]
            if current_sum == target:
                return sorted([sorted_nums[left][0], sorted_nums[right][0]])
            elif current_sum < target:
                left += 1
            else:
                right -= 1