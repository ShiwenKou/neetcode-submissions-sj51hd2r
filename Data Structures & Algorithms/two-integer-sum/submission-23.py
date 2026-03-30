class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # OK they want to return indexes.

        # we use hashmap here.


        seen = {}

        for i in range(len(nums)):

            complement = target - nums[i]
            if complement in seen:
                return [seen[complement], i]
            
            seen[nums[i]] = i
