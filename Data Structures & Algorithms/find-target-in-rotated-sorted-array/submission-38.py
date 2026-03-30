class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # find the sorted part, then see if the target in the sorted area

        left, right = (0, len(nums) - 1)


        while left <= right:

            mid = (left +right) // 2

            if target == nums[mid]:
                return mid

            if nums[mid] >= nums[left]: # sorted, check
                if target >= nums[left] and target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

            elif nums[mid] < nums[left]: # mid to right is sorted

                if target > nums[mid] and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        
        return -1