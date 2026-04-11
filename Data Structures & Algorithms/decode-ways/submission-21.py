class Solution:
    def numDecodings(self, s: str) -> int:
        




        memo = {}
        def dfs(start):

            if start == len(s):
                return 1 # when reach base case, it counts as a valid sol
            if start in memo:
                return memo[start]
            res = 0
            for end in range(start, min(len(s),start + 2)):

                substring = s[start: end + 1]

                if len(substring) == 1 and 1 <= int(substring) <= 9:
                    res = dfs(end + 1)
                
                else:
                    if 10 <= int(substring) <= 26:
                        res = res + dfs(end + 1)
            memo[start] = res
            return res

        return dfs(0)