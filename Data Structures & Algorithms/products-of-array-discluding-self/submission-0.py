class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # the main idea it to iterate forward and backward to maintain a list, 
        #which in forward loops calculates the indexes left product, while the backward to maintain a list to
        # calculate the indexes right product.

        # let's do the first part


        res = [1] * len(nums)
        res_2 = [1] * len(nums)

        for i in range(len(nums)):

            
            if i > 0:
                res[i] = left_product * nums[i - 1]
                left_product = res[i]
            else:
                res[i] = 1
                left_product = res[i]

        for i in range(len(nums)- 1, -1 , -1):

            if i < len(nums) - 1:
                res_2[i] = right_product * nums[i + 1]
                right_product = res_2[i]
            
            else:
                res_2[i] = 1
                right_product = res_2[i]

        return list(i*j for i , j in zip(res, res_2))


        