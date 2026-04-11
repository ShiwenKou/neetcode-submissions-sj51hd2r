class Solution:
    def numDecodings(self, s: str) -> int:
        

        memo = {}
        def dfs(start):

            if start == len(s):
                return 1
            if start in memo:
                return memo[start]

            total = 0

            # for end in range(start, len(s)): # this means each time we can start everywhere cannot. we can only start one or two steps
            for end in range(start, min(start + 2, len(s))):
                sub = s[start: end + 1]

                if len(sub) == 1 and 1 <= int(sub) <= 9:
                    total += dfs(end + 1)

                else:
                    if sub[0] != '0' and 10 <= int(sub) <= 26:
                        total += dfs(end + 1)
            memo[start] = total
            return total
        return dfs(0)