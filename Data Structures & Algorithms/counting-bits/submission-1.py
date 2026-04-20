class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for num in range(n + 1):
            cnt = 0
            while num:

                tmp = num & 1
                cnt += tmp
                num = num >> 1
            
            res.append(cnt)
        return res
