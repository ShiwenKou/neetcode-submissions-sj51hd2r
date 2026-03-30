class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        st = set(nums)
        res = 0
        for n in st:
            tmp = 1
            if n-1 not in st:
                while n + 1 in st:
                    tmp += 1
                    n += 1
                res = max(res, tmp)



        return res