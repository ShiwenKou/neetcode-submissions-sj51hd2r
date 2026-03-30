class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        # this problem we need to use deque, 
        # use the customer analogue to solve this problem
        # first we need to know if the front customer is alr out of line
        # second, we need to know if the current customer is the richest. If it is, the front customer will never get served.

        # if line if windows is reached, we popleft.


        from collections import deque

        res = []
        dq = deque()

        # note that, we only store indexes inside this dq

        # check if the front customer is alr out of window

        for i in range(len(nums)):

            # for exmaple,

            while dq and dq[0] < i - k + 1: # if k=3 i=2, means the window just get full
                dq.popleft()

            while dq and nums[i] > nums[dq[-1]]: # if new come customer greater than the last one in queue, remove it.
                dq.pop()
            dq.append(i)

            if i >= k - 1:
                res.append(nums[dq[0]])
            
        return res





        