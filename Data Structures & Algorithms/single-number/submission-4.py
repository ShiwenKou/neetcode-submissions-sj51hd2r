class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0 # ^ anything keep that

        for n in nums:
            res = res ^ n

        return res