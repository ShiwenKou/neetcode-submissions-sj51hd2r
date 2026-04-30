class Solution:
    def reverse(self, x: int) -> int:
        max_int = 0x7FFFFFFF

        if x >= 0:
            sign = 1
        else:
            sign = -1
        res = 0
        x = abs(x)
        while x:
            val = x % 10
            res = res * 10 + val
            x = x // 10
        

        if res > 0x7FFFFFFF:
            return 0

        return res * sign

        