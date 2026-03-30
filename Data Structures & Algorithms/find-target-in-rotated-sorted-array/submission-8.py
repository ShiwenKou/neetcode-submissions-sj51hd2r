class Solution:
    def search(self, nums: List[int], target: int) -> int:


        # ok this problem is about finding the invariants.


        left, right = (0, len(nums)- 1)

        while left <= right:

            mid = (left + right) // 2


            if target == nums[mid]:
                return mid

            if nums[mid] >= nums[right]:

                # the mid pointer is located at the left portion.

                # we need to make sure whether the target is within left to mid
                if target >= nums[left] and target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            
            else: # nums[mid] < nums[right]: This means the middle pointer is at the right portion.

                if target > nums[mid] and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return - 1


