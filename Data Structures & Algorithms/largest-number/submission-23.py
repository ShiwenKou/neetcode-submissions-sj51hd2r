class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        from functools import cmp_to_key

        lst = list(map(str, nums))

        new = sorted(lst, key=cmp_to_key(lambda x1, x2: 1 if x1 + x2 < x2 + x1 else -1))

        return str(int(''.join(new)))