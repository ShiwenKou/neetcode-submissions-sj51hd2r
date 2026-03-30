class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # 2/20
        max_res = 0
        for i in range(len(heights)):

            for j in range(i+1, len(heights)):

                max_res = max(min(heights[i],heights[j])*abs(j-i), max_res)
        return max_res
