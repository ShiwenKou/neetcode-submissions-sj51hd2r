class Solution:
    def search(self, nums: List[int], target: int) -> int:
        

        left, right = 0, len(nums) - 1

        while left <= right: # we are searching, not looking for pairs

            mid = (left + right) // 2
            if target == nums[mid]:
                return mid

            if nums[mid] >= nums[left]: # this may be trivial
                if target < nums[mid] and target >= nums[left]:
                    right = mid -1
                else:
                    left = mid + 1
            
            else:
                if target <= nums[right] and target > nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1
