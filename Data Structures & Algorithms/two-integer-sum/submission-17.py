class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # is the nums is sorted, we can also use two pointers to solve it .


        # first sort the nums

        # nums = sorted(nums)# in place sort with O(logn) # if we sort like this, we lose its original index.

        # l, r = 0, len(nums) - 1

        # while l < r: # since we are looking for a pair

        #     if nums[l] + nums[r] == target:
        #         break
            
        #     elif nums[l] + nums[r] > target:
        #         r -= 1
        #     else:
        #         l += 1
        # return [l,r]



        sorted_nums = sorted((v, i) for i,v in enumerate(nums))

        l, r = 0, len(sorted_nums) - 1

        while l < r:

            if sorted_nums[l][0] + sorted_nums[r][0] == target:
                return sorted([sorted_nums[l][1],sorted_nums[r][1]]) # return the answer with the smaller index first.

            elif sorted_nums[l][0] + sorted_nums[r][0] > target:
                r -= 1
            else:
                l += 1

        


