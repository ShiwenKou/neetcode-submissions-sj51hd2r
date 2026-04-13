class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        

        ans = nums[0]
        curSum = 0

        for n in nums:
            if curSum < 0:
                curSum = 0
            
            curSum += n
            ans = max(ans, curSum)
        return ans