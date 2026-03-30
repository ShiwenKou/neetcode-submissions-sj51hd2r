class Solution:
    def trap(self, height: List[int]) -> int:

        # this one is not hard at all, we only need to iterate each bar to see how many water we can trap

        left_max = 0
        right_max = 0


        left, right = 0, len(height) - 1
        total = 0
        while left <= right: # this is not a pair, so we need to take each bar into account

            if height[left] < height[right]: # this means the bottleneck is on the left

                left_max = max(left_max, height[left])
                total += left_max - height[left]

                left += 1
            else:
                right_max = max(right_max, height[right])
                total += right_max - height[right]

                right -= 1
        return total

        