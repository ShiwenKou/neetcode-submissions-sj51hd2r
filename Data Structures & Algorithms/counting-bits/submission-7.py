class Solution:
    def countBits(self, n: int) -> List[int]:
        
        memo = [0] * (n + 1)

        offset = 1

        for i in range(1, n + 1): # memo[0] is base

            if offset * 2 == i:
                offset = i
            
            memo[i] = 1 + memo[i - offset]

        return memo

