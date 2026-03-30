class Solution:
    def findMin(self, nums: List[int]) -> int:
        

        left, right = (0, len(nums) - 1)


        res = nums[left]


        while left <= right:

            mid = (left + right) // 2

            res = min(res, nums[mid])


            if nums[mid] >= nums[left]: # left to mid is sorted, we want the unsorted part.
                res = min(res, nums[left]) 
                left = mid + 1
            else: # nums[mid] < nums[left]  this is the unsorted part
                right = mid - 1
        return res

