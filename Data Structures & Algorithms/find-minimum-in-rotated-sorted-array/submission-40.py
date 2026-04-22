class Solution:
    def findMin(self, nums: List[int]) -> int:
        

        # the pivots resides in the unsorted part
        # we can easily find the unsorted part


        left, right = 0, len(nums) - 1
        res = nums[0]
        while left <= right: # we are doing searching here, so we use <=

            mid = (left + right) // 2 # python can handle large number

            res = min(res, nums[mid])

            if nums[mid] >= nums[right]: # unsorted part within mid + 1 to right inclusive

                left = mid + 1
            else: # verse vesa

                right = mid - 1
        return res