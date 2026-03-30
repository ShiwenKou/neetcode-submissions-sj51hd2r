class Solution:
    def findMin(self, nums: List[int]) -> int:

        # this problem has two solutions comparing with the left has a edge case

        left, right = (0, len(nums) - 1)

        res = float('inf')
        while left <= right:

            m = (left + right) // 2

            res = min(nums[m], res)

            if nums[m] >= nums[left]:
                # this suggest that pointer m and left are in the same portion, the minimum is either at pointer left, or from m+1 to right
                res = min(res, nums[left])
                left = m + 1
            elif nums[m] < nums[left]:

                # m and left are in different portion
                # everything from m+ 1 to the end will only greate than num[m], so we shrink the right side by
                right = m - 1
        return res
        