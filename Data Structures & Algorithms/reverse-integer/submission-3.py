class Solution:
    def reverse(self, x: int) -> int:
        if x >= 0:
            sign = 1
        else:
            sign = -1
        max_int = 0x7FFFFFFF

        res = 0
        x = abs(x)
        while x:
            val = x % 10
            res = res * 10 + val
            x = x // 10
        
        if res > max_int:
            return 0
        else:
            return res * sign