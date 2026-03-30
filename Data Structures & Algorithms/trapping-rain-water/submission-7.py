class Solution:
    def trap(self, height: List[int]) -> int:


        max_left = height[0]

        max_right = height[-1]

        left = 0
        right = len(height) - 1

        total = 0

        while left < right:
            if height[left] < height[right]: # max_left = height[left] < height[right] = max_right
            # so max_left < max_right, the max_left is the bottleneck.

                max_left = max(max_left, height[left])

                total += max_left - height[left]
                left += 1
            else: #max_left = height[left] >= height[right] = max_right
            # max_left >= max_right for pointer right, max_right is the bottleneck.
                max_right = max(max_right, height[right])
                total += max_right - height[right]
                right -= 1

        
        return total
        