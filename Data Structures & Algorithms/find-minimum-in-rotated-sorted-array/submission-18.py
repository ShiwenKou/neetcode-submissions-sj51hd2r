class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = (0, len(nums) - 1)

        res = float('inf')


        while left <= right:

            mid = (left + right) // 2

            res = min(res, nums[mid])


            if nums[mid] < nums[left]: # mid in the right portion

                right = mid - 1
            else: # nums[mid] >= nums[left]
                res = min(res,nums[left])
                left = mid + 1
        return res