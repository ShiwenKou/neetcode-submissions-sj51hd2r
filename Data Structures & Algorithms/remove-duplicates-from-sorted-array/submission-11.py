class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        # so this one requires in place modification. 

        # we also use a two pointer technique.

        # this is a sorted list, so the first element should be okay

        # we use one pointer the denote the next modifier/index

        # we use another to see if violations occurs.


        l = 1

        for r in range(1, len(nums)):

            if nums[r] != nums[r - 1]:
                nums[l] = nums[r]
                l += 1
            # l will move automatically

        return l