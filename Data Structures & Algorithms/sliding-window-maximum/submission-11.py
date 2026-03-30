class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        from collections import deque

        l = r = 0

        dq = deque()
        res = []
        while r < len(nums):

            # make sure window valid # r -k + 1 is the start index
            
            while dq and dq[0] < r - k + 1:
                dq.popleft()
            # make sure greater r be at index 0
            while dq and nums[dq[-1]] < nums[r]:
                dq.pop()

            dq.append(r)
            if r >= k -1:
                res.append(nums[dq[0]])
            r += 1
        return res

