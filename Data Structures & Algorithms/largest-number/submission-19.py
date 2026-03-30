from functools import cmp_to_key
class Solution:
    def largestNumber(self, nums: List[int]) -> str:

        lst = list(map(str, nums))

        res = sorted(lst, key=cmp_to_key(lambda x1, x2: -1 if x1+x2 > x2+x1 else 1))

        return str(int(''.join(res)))

        