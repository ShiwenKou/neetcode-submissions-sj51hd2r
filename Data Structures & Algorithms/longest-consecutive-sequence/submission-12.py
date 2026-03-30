class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        st = set(nums)
        length = 0
        res = 0
        for n in st:
            if n - 1 not in st:
                length = 1
                start = n
                while start + 1 in st:
                    length += 1
                    start += 1

                res = max(res, length)
        return res
        