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

                #  mid in the right portion

                # if target > nums[mid] and target <= nums[right]:
                #     left = mid + 1
                # else:
                #     right = mid - 1
                
                # # or mid in the left portion

                # if target < nums[mid] and target >= nums[left]:
                #     right = mid - 1
                # else:
                #     left = mid + 1

                # the above two situation can be put together as:
                # if (target > nums[mid] and target <= nums[right]) or not(target < nums[mid] and target >= nums[left]):
                # # we can simplify the above first use de morgan's rule

                # if (target > nums[mid] and target <= nums[right]) or (target >= nums[mid] or target < nums[left]):
                # then we assume target > nums[mid] = A , target <= nums[right] = B, target >=nums[mid] =A. target < nums[left] = can
                # then we have (A and B) or (A and C) absorbtion law, if (A implies B) then we can keep be
                # thus if (A and B) = True then (A and C) will be True. As a result,  (A and B) or (A and C) = (A and C)
                if target < nums[mid] and target >= nums[left]:
                    right = mid - 1
                else:
                    left = mid + 1
            
            else: #nums[mid] < nums[left] mid in the right portion
                if target > nums[mid] and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid -1

        return -1


            
