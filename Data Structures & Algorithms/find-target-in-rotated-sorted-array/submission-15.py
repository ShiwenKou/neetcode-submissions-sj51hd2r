class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = (0, len(nums) -1 )


        while left <= right: # this is cuz we need to check every value

            mid = (left + right) // 2
            if target == nums[mid]:
                return mid

            if nums[mid] >= nums[left]:
                # this means the mid and left are in the same portion but don't know right portion or left portion.

                # there exist an edge case at pointer left now.

                #let's assume they are in the right portion by (target > nums[mid] and target <=nums[right])
                
                # and then assume they are in the left portion by not(target < nums[mid] and target >=nums[left])
                if target > nums[mid] or target <nums[left]:
                    left = mid + 1
                else:
                    right = mid - 1
                

            else: #nums[mid] < nums[left] , this means mid in right portion

                if target > nums[mid] and target <= nums[right]:
                    left = mid + 1
                else:

                    right = mid - 1
        return - 1