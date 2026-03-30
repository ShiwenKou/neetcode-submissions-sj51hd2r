class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ans = 0
        for i in range(len(heights)):
            for j in range(len(heights)):

                area = abs(i-j) * min(heights[i], heights[j])

                ans = max(ans, area)
        return ans
        