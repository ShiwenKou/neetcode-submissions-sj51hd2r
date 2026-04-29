class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        
        from functools import cmp_to_key

        res = sorted(map(str, nums), key=cmp_to_key(lambda x1, x2:1 if x1 + x2 < x2 + x1 else -1))
        res = ''.join(res)
        return res if res[0] != '0' else '0'
