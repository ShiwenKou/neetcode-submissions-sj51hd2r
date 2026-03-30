class Solution:
    def findMin(self, nums: List[int]) -> int:
        # so this problem we just need to remember a invariant 

        left, right = (0 , len(nums) - 1)

        res = float('inf')


        while left <= right:

            mid = (left + right) // 2

            res = min(res, nums[mid])


            if nums[mid] >= nums[right]: # this this is the case, mid in the left portion

                # and the left portion is always going to be greater than the right portion
                left = mid + 1
            else: # nums[mid] < nums[right] mid in the right portion every element from index m+ 1 to right shld be crossed out

                right = mid - 1
        return res

