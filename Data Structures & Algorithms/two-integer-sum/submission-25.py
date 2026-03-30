class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # OK they want to return indexes.

        # we use hashmap here.


        # seen = {}

        # for i in range(len(nums)):

        #     complement = target - nums[i]
        #     if complement in seen:
        #         return [seen[complement], i]
            
        #     seen[nums[i]] = i

        # we can also solve this by using two pointers.

        # but remember they want if we want two pointers two work. the list has to be sorted.
        # and cuz they want the indexes. so the orignal index should also be preserved.


        sorted_nums = sorted((v, i) for i, v in enumerate(nums))

        l, r = 0, len(nums) - 1

        while l < r:

            if sorted_nums[l][0] + sorted_nums[r][0] == target:
                return sorted([sorted_nums[l][1], sorted_nums[r][1]])
            
            elif sorted_nums[l][0] + sorted_nums[r][0] > target:
                r -= 1
            else:
                l += 1
        
