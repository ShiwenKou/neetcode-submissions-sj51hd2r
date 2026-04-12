class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        import sys
        sys.setrecursionlimit(10000)
        memo = {}
        def dfs(r, c):

            if c == len(t):
                return 1
            if r == len(s):
                return 0
            if (r, c) in memo:
                return memo[(r, c)]

            res = 0
            res += dfs(r + 1, c)
            if s[r] == t[c]:
                res += dfs(r+1, c+1)
                


            memo[(r, c)] = res
            return res
        return dfs(0, 0)
