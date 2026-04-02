class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        

        def findIdx(left, right, leftMost):
            res = -1
            while left <= right:
                mid = (left + right) // 2

                if nums[mid] > target:
                    right = mid - 1
                elif nums[mid] < target:
                    left= mid + 1
                else:
                    res = mid
                    if leftMost:
                        right = mid - 1
                    else:
                        left = mid + 1
            return res
        
        res1 = findIdx(0, len(nums) - 1, True)
        res2 = findIdx(0, len(nums) - 1, False)
        return [res1, res2]