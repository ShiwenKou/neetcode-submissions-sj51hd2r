class Solution:
    def findMin(self, nums: List[int]) -> int:

        # for this problem, we have two solutions. one has a edge case

        # left, right = (0, len(nums) - 1)

        # res = float('inf')
        # while left <= right:

        #     m = (left + right) // 2

        #     res = min(res, nums[m])

        #     if nums[m] >= nums[left]:
        #         # m and left are in the same portion. but we don't exactly know it is in the left or right portion
        #         res = min(res, nums[left])
        #         left = m + 1
        #     elif nums[m] < nums[left]:
        #         # m in the right portion while left in the left portion.  and if m in the right portion we know. m+1 to the right all greater then the value at index m
        #         right = m - 1
        # return res


        left, right =(0, len(nums)- 1)

        res = float('inf')

        while left <= right:

            m = (left + right) // 2

            res = min(res, nums[m])

            if nums[m] >= nums[right]:

                # m in the left portion, right in the right portion. 
                # everything on the left portion is always going to be greater than the right portion

                left = m + 1
            elif nums[m] < nums[right]:

                # m and right are in the same portion.

                # we can simply cross out all the value between index m to right
                right = m - 1
        return res
            
        