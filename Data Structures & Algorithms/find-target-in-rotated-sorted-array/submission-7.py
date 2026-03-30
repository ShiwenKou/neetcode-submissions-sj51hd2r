class Solution:
    def search(self, nums: List[int], target: int) -> int:


        # ok this one is not hard !!!


        left, right = (0, len(nums) - 1)


        while left <= right:

            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            if nums[mid] >= nums[right]: # this means mid in left portion. while index right in right portion

                # we then need to decide search left or right

                if target < nums[mid] and target >= nums[left]: # we check if the target in the left portion
                    right = mid - 1
                
                else:
                    left = mid + 1
            else: # nums[mid] < nums[right] # this means mid in the right portion


                if target > nums[mid] and target <= nums[right]: # we check if the target in the right portion
                    left = mid + 1
                
                else:
                    right = mid - 1
        return -1

        