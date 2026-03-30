class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # # 2/20
        # max_res = 0
        # for i in range(len(heights)):

        #     for j in range(i+1, len(heights)):

        #         max_res = max(min(heights[i],heights[j])*abs(j-i), max_res)
        # return max_res

        # 2/20

        # as u can see, in min(height[i], heights[j]). Once the bottleneck is fixed, scanning other bar is useless.
        # so here we use a two pointer tehcnique.


        l,r = 0, len(heights) - 1
        max_res = 0
        # because, this is a two pair proble, so we use while l < r

        while l < r:

            max_res = max(min(heights[l],heights[r])*abs(r-l), max_res)

            if heights[l] < heights[r]:
                # this means l is the bottle neck, we can remove it.
                l += 1
            else:

                r -= 1
        return max_res

            
