class Solution:
    def trap(self, height: List[int]) -> int:

        if len(height) == 0 : return 0

        left = 0
        right = len(height) - 1

        max_left = 0
        max_right = 0
        total = 0
        while left <= right:

            if max_left < max_right:

                max_left = max(max_left, height[left])
                total += max_left - height[left]
                left += 1
            
            else:
                max_right = max(max_right, height[right])
                total += max_right - height[right]
                right -= 1

        return total


        