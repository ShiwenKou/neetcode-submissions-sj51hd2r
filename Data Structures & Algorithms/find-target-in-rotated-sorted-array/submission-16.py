class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = (0, len(nums) -1 )


        # let's code the left comparison again

        left, right = (0, len(nums) - 1)

        while left <= right:

            mid = (left + right) // 2

            if target == nums[mid]:
                return mid
            
            if nums[mid] >= nums[left]: # this is the right order , so mid could be in the left or the right portion ascending 

                # if mid in the right portion

                # if target > nums[mid] and target <= nums[right]:
                #     left = mid + 1
                # else:
                #     right = mid - 1
                
                # # if mid in the left portion

                # if target < nums[mid] and target >= nums[left]:
                #     right = mid - 1
                # else:
                #     left = mid + 1

                # the above two situation can be put together as:
                if (target > nums[mid] and target <= nums[right]) or not(target < nums[mid] and target >= nums[left]):
                    left = mid + 1
                else:
                    right = mid - 1
            
            else: #nums[mid] < nums[left] mid in the right portion
                if target > nums[mid] and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid -1

        return -1


            
