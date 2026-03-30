class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # the brute force solution is disastrous with time complexity of n!
        # there is actually a trick for this questionin 3 steps

        # 1. we reversely iterate the list to to find the first element that is less than its last element.
        #  find the pivot.
        # 2. find successor
        # reversely iterate the list again and find the immediate greater element for the pivot 
        # swap them

        # 3. swap the sublist, from i+1 to the end.


        i = len(nums) - 2

        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        
        if i > 0: # in this conditiion, we find the successor

            j = len(nums) - 1

            while j > i and nums[j] <= nums[i]:
                j -= 1
            
            nums[i], nums[j] = nums[j], nums[i]

        
        l, r = i + 1, len(nums) - 1

        while l < r: # this is a pair, so we can safely use l < r

            nums[l], nums[r] = nums[r], nums[l]

            l += 1
        
            r -= 1



