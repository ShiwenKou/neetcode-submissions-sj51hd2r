class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        

        from functools import cache
        @cache
        def dfs(r, c):

            if c == len(t):
                return 1
            if r == len(s):
                return 0
            # if (r, c) in memo:
            #     return memo[(r, c)]

            res = 0
            for i in range(r, len(s)):
                if s[i] == t[c]:
                    res += dfs(i + 1, c + 1)
            # memo[(r, c)] = res
            return res
        return dfs(0, 0)
