class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        
        from functools import cmp_to_key
        res = [str(c) for c in nums]
        res = sorted(res, key=cmp_to_key(lambda x1, x2: 1 if x1 + x2 < x2 + x1 else -1))

        return str(int(''.join(res)))