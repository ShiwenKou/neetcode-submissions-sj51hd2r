class Solution:
    def findMin(self, nums: List[int]) -> int:

        # for this problem, we have two solutions. one has a edge case

        left, right = (0, len(nums) - 1)

        res = float('inf')
        while left <= right:

            m = (left + right) // 2

            res = min(res, nums[m])

            if nums[m] >= nums[left]:
                # m and left are in the same portion. but we don't exactly know it is in the left or right portion
                res = min(res, nums[left])
                left = m + 1
            elif nums[m] < nums[left]:
                # m in the right portion while left in the left portion. 
                right = m - 1
        return res
            
        