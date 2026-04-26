class Solution:
    def reverseBits(self, n: int) -> int:
        

        res = 0
        for i in range(32):

            bit = (n & 1) << 31 - i

            res = res | bit
            n = n >> 1
        return res