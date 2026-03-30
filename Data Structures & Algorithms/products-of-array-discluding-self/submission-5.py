class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prefix = [1] * len(nums)
        postfix = [1] * len(nums)
        res = []

        for i in range(len(nums)):
            prefix[i] = prefix[i-1] * nums[i-1]  if i > 0 else 1
        
        for i in range(len(nums)-1,-1,-1):
            postfix[i] = nums[i+1] * postfix[i+1] if i < len(nums) - 1 else 1
        for i in range(len(nums)):
            res.append(prefix[i]*postfix[i])
        return res