class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # we also take advantage of the invariant


        left, right = (0, len(nums) - 1)

        while left <= right:

            mid = (left + right) // 2

            if target == nums[mid]:
                return mid
            

            if nums[mid] >= nums[right]:

                # mid in the left portion.

                if target >= nums[left] and target < nums[mid]: # make sure if target is here
                    right = mid - 1
                else: # target is not there

                    left = mid + 1
            elif nums[mid] < nums[right]: # mid in the right portion
                if target > nums[mid] and target <=nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return - 1


        