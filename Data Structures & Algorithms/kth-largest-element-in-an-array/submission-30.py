class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k
        import random
        def quickSort(left, right):
            
            idx = random.randint(left, right)
            nums[idx], nums[right] = nums[right], nums[idx]
            
            pivot = nums[right]
            p = left
            for i in range(left, right):

                if nums[i] <= pivot:
                    nums[i], nums[p] = nums[p], nums[i]
                    p += 1
            nums[right], nums[p] = nums[p], nums[right]
            if k > p:
                return quickSort(p + 1, right)
            elif k < p:
                return quickSort(left, p - 1)
            else:
                return nums[p]
        
        return quickSort(0, len(nums) - 1)