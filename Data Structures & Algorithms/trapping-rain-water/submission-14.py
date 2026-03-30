class Solution:
    def trap(self, height: List[int]) -> int:

        left = 0
        right = len(height) - 1

        max_left = 0
        max_right = 0


        total = 0

        while left < right: # as we are dealing with individual positions not pairs. so we need to consider situation when left == right

            if height[left] < height[right]: # it means max_left <=height[left] < height[right]
            # so max_left now is the lower bound

                max_left = max(max_left, height[left])
                total += max_left - height[left]
                left += 1
            else:

                max_right = max(max_right, height[right])
                total += max_right - height[right]
                right -= 1
        return total

        