class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prefix = []
        postfix = [1] * len(nums)
        res = []

        for i in range(len(nums)):

            val = nums[i - 1] * prefix[i - 1] if i > 0 else 1
            prefix.append(val)


        for i in range(len(nums) - 1, -1, -1):

            val = nums[i + 1] * postfix[i + 1] if i < len(nums) - 1 else 1
            postfix[i] = val
        
        for i in range(len(prefix)):
            res.append(prefix[i] * postfix[i])
        return res




            
        