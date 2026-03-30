class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # this problem we can use a brute force approach to solve.

        res = 0
        for i in range(len(heights)):

            for j in range(i+1, len(heights)):

                res = max(res, (j - i) * min(heights[i],heights[j]))
        return res
