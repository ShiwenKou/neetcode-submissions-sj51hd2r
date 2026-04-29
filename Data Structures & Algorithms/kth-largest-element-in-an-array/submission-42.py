class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import random
        k = len(nums) - k
        def quickSelect(left, right):
            n = random.randint(left, right)
            nums[n], nums[right] = nums[right], nums[n]
            p = left
            pivot = nums[right]
            for i in range(left, right):
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1
            
            nums[p], nums[right] = nums[right], nums[p]


            if p < k:
                return quickSelect(p + 1, right)

            elif p > k:
                return quickSelect(left, p - 1)

            else:
                return nums[p]
        
        left, right = 0, len(nums) - 1

        return quickSelect(left, right)
                