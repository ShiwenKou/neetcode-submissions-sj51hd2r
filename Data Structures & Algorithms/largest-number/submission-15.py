class Solution:
    def largestNumber(self, nums: List[int]) -> str:

        from functools import cmp_to_key

        res = list(map(str,nums))

        ans = sorted(res,key=cmp_to_key(lambda x1,x2: -1 if x1+x2 > x2+x2 else 1))

        return str(int(''.join(ans)))
        