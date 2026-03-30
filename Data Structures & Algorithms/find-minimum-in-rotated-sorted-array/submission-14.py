class Solution:
    def findMin(self, nums: List[int]) -> int:
        # so this problem we just need to remember a invariant .


        left , right = (0, len(nums) - 1)

        res = nums[0]

        while left <= right: # because we need to see every element, not every pair

            mid = (left + right ) // 2

            res = min(res, nums[mid])


            if nums[mid] >= nums[left]: # this one has two possibilities. mid in the left portion or right portion

                # we assume they are in the right portion, after we check it's left pointer

                res = min(res, nums[left])
                left = mid + 1

            else:# nums[mid] < nums[left]: # mid in the right portion. every element from mid to right need to be crossed out

                right = mid - 1

        return res
        

        