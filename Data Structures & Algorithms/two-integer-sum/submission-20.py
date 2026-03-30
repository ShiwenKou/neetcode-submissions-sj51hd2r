class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # this problem we have two solutions. one use hashmap anothe one use two pointer techniques.


        seen = {}

        for i in range(len(nums)):

            complement = target - nums[i]

            if complement in seen:

                return [seen[complement], i]
            
            seen[nums[i]] = i


