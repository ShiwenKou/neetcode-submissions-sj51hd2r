class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def findIndex(left, right, flag):
            res = -1
            while left <= right:
                mid = (left + right) // 2

                if nums[mid] > target:
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    res = mid
                    if flag == -1:
                        right = mid - 1
                    else:
                        left = mid + 1
            return res

        res1 = findIndex(0, len(nums) - 1, -1)
        res2 = findIndex(0, len(nums) - 1, 1)

        return [res1, res2]
       
        



            