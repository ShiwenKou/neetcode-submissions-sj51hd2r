class Solution:
    def trap(self, height: List[int]) -> int:
        # let's try the most understandable solution.

        # we need to list to main all the max_left and max_right at each position.


        left_list = [0] * len(height)
        right_list = [0] * len(height)

        max_left = height[0]
        max_right = height[-1]
        total = 0
        for i in range(len(height)):

            max_left = max(max_left, height[i])

            left_list[i] = max_left
        for i in range(len(height) - 1, -1, -1):
            max_right = max(max_right, height[i])

            total += min(left_list[i], max_right) - height[i]

        return total
