class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        # use dq to maintain a fixed window
        # remove the first one when the window if full
        # if the new come one if greater than the last one, remove the last one.
        # return the first one in queue when the index is greater than k - 1


        from collections import deque

        dq = deque()
        res = []

        for i in range(len(nums)):

            while dq and dq[0] < i - k + 1: # this is the start index of the next window
                dq.popleft()
            
            while dq and nums[dq[-1]] < nums[i]: # new customer is greater than the last one in queue.
                dq.pop() # make sure the greatest num is in the front

            
            dq.append(i)


            if i >= k - 1:
                res.append(nums[dq[0]])
        return res

    