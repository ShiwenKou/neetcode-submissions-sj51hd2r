class Solution:
    def reverse(self, x: int) -> int:
        max_int = 0x7FFFFFFF
        if x >= 0:
            sign = 1
        
        else:
            sign = -1

        x = abs(x)
        res = 0
        while x:
            val = x % 10

            x = x // 10

            res = res * 10 + val

        if res > max_int:
            return 0

        else:
            return res * sign

        