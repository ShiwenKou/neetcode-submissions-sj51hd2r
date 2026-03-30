class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left, right = (0, len(nums)-1)


        while left <= right:

            mid = (left + right) // 2

            if target == nums[mid]:
                return mid
            

            if nums[mid] >= nums[right]: # left to mid is sorted

                if target >= nums[left] and target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            
            elif nums[mid] < nums[right]: # mid to right is sorted
                if target > nums[mid] and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1
