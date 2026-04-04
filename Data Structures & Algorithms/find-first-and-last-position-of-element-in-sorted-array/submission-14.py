class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res = []
        def binarySearch(left, right, flag):
            res = -1
            while left <= right:
                mid = (left + right) // 2

                if nums[mid] > target:
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    res = mid
                    if flag: # left most
                        right = mid - 1
                    else: # right most
                        left = mid + 1
            return res
        return [binarySearch(0, len(nums) - 1, True), binarySearch(0, len(nums) - 1, False)]