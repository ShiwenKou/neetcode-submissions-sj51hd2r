class Solution:
    def getSum(self, a: int, b: int) -> int:
        
        max_int = 0x7FFFFFFF
        mask = 0xFFFFFFFF

        while b != 0:

            carry = (a & b) << 1
            a = (a ^ b) & mask
            b = carry & mask
        
        return a if a <= max_int else ~(a ^ mask)
        # 当且仅当a小于等于max_int的时候我们返回a本身。否者需要对a两次取反，不然python会以为a是个超大整数。第一次取反是临时操作。第二次取反是为了中和第一次取反的前提下，把a前面全部加上1表示负数