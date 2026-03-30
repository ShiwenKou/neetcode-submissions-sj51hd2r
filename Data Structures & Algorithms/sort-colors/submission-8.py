class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # this problem we want to put 0 to the left pointer, while swap the 2s to the right pointer.

        # invariant [0,left) -> 0s [left,i) -> all 1s (right,-1] all 2s i,left unknow.


        left, right, i = (0, len(nums) -1 ,0)

        while i <= right: # we nned to check i at right index

            if nums[i] == 0: # we do left swap

                nums[i], nums[left] = nums[left], nums[i]
                left += 1 # we know it's 1 from the left swap, safe

            elif nums[i] == 2: # we do right swap
                nums[i], nums[right] = nums[right], nums[i]

                right -= 1
                i -= 1 # we don't know what is from the right swap
            i += 1
