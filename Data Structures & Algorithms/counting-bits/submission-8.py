class Solution:
    def countBits(self, n: int) -> List[int]:
        
        offset = 1
        memo = [0] * (n + 1)

        for i in range(1, n + 1):
            if offset * 2 == i:
                offset = i
            
            memo[i] = 1 + memo[i - offset]
        return memo