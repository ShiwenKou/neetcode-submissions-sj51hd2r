class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        from functools import cache
        @cache
        def dfs(r, c):
            if c == len(p):
                return r == len(s)

            first_match = r < len(s) and (s[r] == p[c] or p[c] == '.')

            if c + 1 < len(p) and p[c + 1] == '*':
                return dfs(r, c + 2) or (first_match and dfs(r + 1, c))
            else:
                return first_match and dfs(r + 1, c + 1)

        return dfs(0, 0)