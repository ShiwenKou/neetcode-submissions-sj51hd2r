class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # so this trik is that, we firstly figure out what all the left_product an all the right_product, things shld get more easier.
        answer = [1] * len(nums)
        left_product = 1
        for i in range(len(nums)):
            answer[i] = left_product

            left_product = left_product * nums[i]
        
        right_product = 1

        for i in range(len(nums) - 1, -1 ,-1):
            answer[i] = answer[i] * right_product
            right_product = right_product * nums[i]
        return answer