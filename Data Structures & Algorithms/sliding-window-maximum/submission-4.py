class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        from collections import deque

        dq = deque()

        res = []


        for i in range(len(nums)):

            # we need to firstly check if the first customer in the queue is out of window

            # the starter window is at i - k + 1

            while dq and dq[0] < i - k + 1: # it means whether if the first customer is out of window, we then pop it
                dq.popleft()

            
            while dq and nums[i] > nums[dq[-1]]:
                dq.pop()

            dq.append(i)

            if i >= k - 1: # the first time window full
                res.append(nums[dq[0]])
        return res
