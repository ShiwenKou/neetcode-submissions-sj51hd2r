class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        st = set(nums)
        res = 0
        for n in st:
            if n - 1 not in st:

                start = n
                cnt = 1

                while start + 1 in st:
                    start = start + 1
                    cnt += 1
                res = max(res, cnt)
        return res