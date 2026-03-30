class Solution:
    def trap(self, height: List[int]) -> int:


        if len(height) == 0:
            return 0
        
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]

        total = 0

        while left < right:

            right_max = max(right_max, height[right])

            if height[left] < right_max:
                left_max = max(left_max, height[left])
                total += left_max - height[left]
                left += 1
            else:
                right_max = max(right_max, height[right])
                total += right_max - height[right]
                right -= 1
        return total        