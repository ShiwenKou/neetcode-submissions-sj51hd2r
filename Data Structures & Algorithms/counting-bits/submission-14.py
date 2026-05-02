class Solution:
    def countBits(self, n: int) -> List[int]:
        
        memo = [0] * (n + 1)

        offset = 1

        for i in range(1, len(memo)):
            if offset * 2 == i:
                offset = i

            memo[i] = 1 + memo[i - offset]
        return memo



        # 0 - 000
        # 1 - 001 <-
        # 2 - 010
        # 3 - 011
        # 4 - 100 <-
        # 5 - 101
        # 6 - 110
        # 7 - 111
        # 8 - 1000 <-