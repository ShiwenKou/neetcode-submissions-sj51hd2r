class Solution:
    def reverse(self, x: int) -> int:
        max_int = 0x7FFFFFFF
        # 1. 记录符号，并把 x 变为正数
        sign = 1 if x >= 0 else -1
        x = abs(x)
        
        res = 0
        while x != 0:
            # 2. 弹出最后一位
            pop = x % 10
            x //= 10
            
            # 3. 压入结果
            res = res * 10 + pop
        if res > max_int:
            return 0
            
        return res * sign