class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        k = len(nums) - k

        def quickSelect(left, right):
            import random

            n = random.randint(left, right)
            nums[n], nums[right] = nums[right], nums[n]

            pivot = nums[right]
            p = left

            for i in range(left, right): # right exclusive

                if nums[i] <= pivot:
                    nums[i], nums[p] = nums[p], nums[i]
                    p += 1
            
            nums[p], nums[right] = nums[right], nums[p]
            if k > p:
                return quickSelect(p + 1, right)
            if k < p:
                return quickSelect(left, p - 1)
            else:
                return nums[p]
        return quickSelect(0, len(nums) - 1)
