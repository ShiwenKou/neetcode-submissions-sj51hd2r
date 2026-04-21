class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        mapping = {}

        for i, n in enumerate(nums):

            complement = target - n

            if complement in mapping:
                return [mapping[complement], i]
            mapping[n] = i
            
            

