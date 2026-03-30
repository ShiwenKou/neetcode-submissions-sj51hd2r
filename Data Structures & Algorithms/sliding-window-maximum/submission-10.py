class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        from collections import deque


        dq = deque()
        res = []
        for i in range(len(nums)):

            while dq and dq[0] < i - k + 1:
                dq.popleft()

            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()
            dq.append(i)


            if i >= k - 1: # record
                res.append(nums[dq[0]])
        return res


        