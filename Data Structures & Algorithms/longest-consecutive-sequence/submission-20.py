class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        st = set(nums)
        res = 0
        for n in st:
            if n - 1 not in st:
                start = n
                length = 1
                while start + 1 in st:
                    start += 1
                    length += 1

                res = max(res, length)
        return res