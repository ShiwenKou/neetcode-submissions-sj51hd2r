class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        st = set(nums)
        res = 0
        for n in st:
            start = n
            if start - 1 not in st:
                length = 1
                while start + 1 in st:
                    length += 1
                    start = start + 1
                res = max(res, length)
        return res



        