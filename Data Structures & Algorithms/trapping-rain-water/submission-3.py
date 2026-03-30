class Solution:
    def trap(self, height: List[int]) -> int:

        if len(height) == 0:
            return 0
        
        left = 0
        right = len(height) - 1

        max_left = height[left]
        max_right = height[right]
        total = 0
        while left < right: # when not True, means every pod's areas are all checked

            if height[left] < height[right]: # cuz height[right] <= max_right, so if it's True, height[left] < max_right
            # the bottleneck is on max_right. So now we compute max_left
                max_left = max(height[left], max_left)
                total += max_left - height[left]
                left += 1
            else:
                # the bottelneck is max_right, so we need to find pod area at index right
                max_right = max(height[right], max_right)
                total += max_right - height[right]
                right -= 1
        return total
                


