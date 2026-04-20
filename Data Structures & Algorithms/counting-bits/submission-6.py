class Solution:
    def countBits(self, n: int) -> List[int]:
        
        memo = [0] * (n + 1)

        offset = 1

        for i in range(1, n + 1):
            if offset * 2 == i:
                offset  = i
            
            memo[i] = 1 + memo[i - offset]
        return memo


        # 0 0000 0
        # 1 0001 1 + memo[1 - 1]
        # 2 0010 1 + memo[2 - 2]
        # 3 0011 1 + memo[3 - 2]
        # 4 0100 1 + memo[4 - 4]
        # 5 0101
        # 6 0110
        # 7 0111
        # 8 1000
