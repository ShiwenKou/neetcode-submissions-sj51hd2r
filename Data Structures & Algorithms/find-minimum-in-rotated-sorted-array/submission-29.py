class Solution:
    def findMin(self, nums: List[int]) -> int:


        # let's do this problem again

        # so the basic idea is the minimum value is at the pivot. and the pivot is within the unsoroted part.

        left, right = (0, len(nums) - 1)

        res = nums[0]
        while left <= right:

            mid = (left + right) // 2
            res = min(res, nums[mid])

            if nums[mid] < nums[right]: # this is the sorted part, pivot should be at the unsorted part

                right = mid - 1
            else: # nums[mid] >= numsp[right] this is the unsorted part
                left = mid + 1
        return res