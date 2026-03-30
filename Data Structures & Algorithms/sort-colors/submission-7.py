class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """


        # so this problem is we need to use two pointers

        l, i, r = (0,0, len(nums) - 1)

        while i <= r: # we need <= cuz element at index right should also examined.

            if nums[i] == 0:
                nums[i], nums[l] = nums[l], nums[i]
                l += 1
                # we don't need to check here is cuz we are guaranteed that elements within [left, i) = 1 so don't match the two ifs.
            elif nums[i] == 2:
                nums[i],nums[r] = nums[r], nums[i]

                r -= 1
                i -=1 # we check here is because we don't know what get swap over from the left.
            i += 1
        
                
