class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        st = set(nums)
        res = 0
        for i in st:
            if i - 1 not in st:
                tmp = 1
                while i + 1 in st:
                    tmp += 1
                    i += 1
                res = max(res, tmp)

        return res