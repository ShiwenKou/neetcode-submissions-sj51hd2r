class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        st = set(nums)

        res = 0
        
        for n in nums:
            tmp = 1
            curr = n
            while curr+1 in st:
                tmp += 1
                curr += 1
            res = max(res, tmp)
        return res