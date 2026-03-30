class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        left = 0
        right = len(heights) - 1

        ans = 0
        while left < right:  # this is actually looking for pairs, so no need considering left == right


            if heights[left] > heights[right]:

                area = (right - left) * heights[right]

                ans = max(area, ans)
                right -= 1
            else:
                area = (right - left) * heights[left]
                ans = max(area, ans)
                left += 1
        return ans
