class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        st = set(nums)
        res = 0
        for n in st:

            if n - 1 not in st:
                count = 1
                start = n
                while start + 1 in st:
                    count += 1
                    start += 1
                res = max(res, count)
        return res