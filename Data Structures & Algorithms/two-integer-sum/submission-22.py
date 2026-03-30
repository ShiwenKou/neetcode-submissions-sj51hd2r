class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # this problem we have two solutions. one use hashmap anothe one use two pointer techniques.


        # seen = {}

        # for i in range(len(nums)):

        #     complement = target - nums[i]

        #     if complement in seen:

        #         return [seen[complement], i]
            
        #     seen[nums[i]] = i

        # to make the two pointers to work ,we have to sort the nums list first. However, they want the index nums of the original nums list.


        # we need to preserve the index of each value

        sorted_nums = sorted((v, i) for i, v in enumerate(nums)) # we will sort the (v, i) by its values nlogn


        l, r = 0, len(sorted_nums) - 1

        while l < r: # we want pairs so we use l < r. we want exact answer not iterate the whole so we need one check first

            if sorted_nums[l][0] + sorted_nums[r][0] == target:
                return sorted([sorted_nums[l][1],sorted_nums[r][1]]) # nlogn
            elif sorted_nums[l][0] + sorted_nums[r][0] > target:
                r -= 1

            else:
                l += 1
            


