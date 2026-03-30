class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # this problem we can use a brute force approach to solve.

        # res = 0
        # for i in range(len(heights)):

        #     for j in range(i+1, len(heights)):

        #         res = max(res, (j - i) * min(heights[i],heights[j]))
        # return res

        # the above method is not good in comlexities.

        # we can use a two pointer techniques here.

        l, r = 0, len(heights) -1
        res = 0
        while l < r: # cuz we are dealing with a pairs. so, l < r is okay
            res = max(res, min(heights[l], heights[r])*( r - l))
            # this is the best result for the current bottleneck, 

            if heights[l] < heights[r]: # this means heights[l] here is the bottleneck.
                l += 1
            else:
                r -= 1
        return res

