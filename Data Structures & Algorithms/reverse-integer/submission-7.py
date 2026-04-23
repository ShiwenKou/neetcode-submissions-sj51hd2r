class Solution:
    def reverse(self, x: int) -> int:
        

        if x >= 0:
            sign = 1
        else:
            sign = -1

        x = abs(x)
        res = 0
        while x != 0:

            val = x % 10
            res = res * 10 + val
            x = x // 10

        
        if res > 0x7FFFFFFF:
            return 0
        
        return res * sign