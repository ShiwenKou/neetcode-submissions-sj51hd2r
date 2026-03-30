class Solution:
    def findMin(self, nums: List[int]) -> int:

        res = nums[0]

        left, right = (0, len(nums) - 1)

        while left <= right:
            m = (left + right) // 2

            res = min(res, nums[m], nums[left])

            if nums[left] <= nums[m]: # this means from left to m should be cross out
                left = m + 1
            elif nums[left] > nums[m]: # this means from m to right should be corssed out
                right = m - 1
        return res
        