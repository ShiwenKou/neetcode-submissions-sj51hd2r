class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # we want to scan the list only once.
        # we use a set here to do the check if our current nums[index] exist in the set.
        # seen1 = set()

        # for i in range(len(nums)):
            
        #     complement = target - nums[i]
        #     if complement in seen:#

        #         return complement index and i 
            
        #     seen.add(nums[i])


        # the above is the solution, however, they want a list of indexes. set can only contain values. so not good.

        # we can consider using a dict. as a key in the dict is immutable so i think dict.get("key") also only takes O(1)


        seen = {}


        for i in range(len(nums)):

            complement = target -nums[i]

            if seen.get(complement) != None: # here we put values in nums as the key, since int is also immutable so, it's okay
                return [seen[complement], i]
            
            seen[nums[i]] = i



        