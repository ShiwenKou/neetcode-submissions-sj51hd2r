class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        st = set(nums)
        res = 0
        for num in st:

            if num - 1 not in st:
                start = num
                count = 1
                while start + 1 in st:
                    count += 1
                    start += 1
                res = max(res, count)
        return res