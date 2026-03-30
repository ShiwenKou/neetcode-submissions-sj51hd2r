class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        from collections import deque

        dq = deque()
        res = []
        for i in range(len(nums)):
            # out of window

            while dq and dq[0] < i - k + 1: # the first index in dq should be i - k + 1
                dq.popleft()

            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()
            # less than new comers

            dq.append(i)

            if i >= k - 1:
                res.append(nums[dq[0]])
        return res