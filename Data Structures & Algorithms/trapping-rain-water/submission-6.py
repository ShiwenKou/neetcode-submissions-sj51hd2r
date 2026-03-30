class Solution:
    def trap(self, height: List[int]) -> int:

        max_left = height[0]
        left_list = []
        max_right = height[-1]
        right_list = [0] * len(height)
        total = 0
        for i in range(len(height)):

            max_left = max(height[i], max_left)
            left_list.append(max_left)

        for i in range(len(height) - 1, -1, -1):

            max_right = max(height[i], max_right)
            right_list[i] = max_right
        for i in range(len(height)):

            total += min(left_list[i], right_list[i]) - height[i]
        return total

