class Solution:
    def trap(self, height: List[int]) -> int:

        # this problem we use two pointer techniques.

        # we maintain a left_max and right_max. min(left_max, right_max) is the bottole neck for the current bar.


        l, r = 0, len(height) - 1

        left_max = 0
        right_max = 0
        total = 0
        # cuz we are dealing with individual bars. so we use while l < =r

        while l <= r:

            if left_max < right_max:

                left_max = max(left_max, height[l]) # we update the left_max to avoid height[l] > left_max. negative water avoided.

                total += left_max - height[l]

                l += 1
            else:

                right_max = max(right_max, height[r])
                total += right_max - height[r]
                r -= 1
        return total

        