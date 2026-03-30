class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        st = set(nums)
        res = 0
        for num in st:
            if num - 1 not in st:
                length = 1
                while num + 1 in st:
                    length += 1
                    num += 1
                res = max(res, length)
        return res