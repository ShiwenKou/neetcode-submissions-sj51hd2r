class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        

        def helper(left, right, flag):
            res = -1
            while left <= right:
                mid = (left + right) // 2

                if nums[mid] < target:
                    left = mid + 1
                
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    res = mid
                    if flag: # keep search left

                        right = mid - 1
                    else:
                        left = mid + 1
            return res

        
        left, right = 0, len(nums)- 1
        return [helper(left, right, True), helper(left, right, False)]