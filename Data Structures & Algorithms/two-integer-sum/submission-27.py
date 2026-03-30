class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}

        for i,v in enumerate(nums):
            complement = target - v

            if complement in d:
                return [d[complement], i]
            d[v] = i
        