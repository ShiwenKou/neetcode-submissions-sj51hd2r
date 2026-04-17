class Solution:
    def countSubstrings(self, s: str) -> int:
        from functools import cache

        @cache
        def dfs(i, j):

            if i >= j:
                return True
            
            if s[i] != s[j]:
                return False
            
            res = dfs(i + 1, j - 1)

            return res

        cnt = 0

        for i in range(len(s)):
            for j in range(i, len(s)):
                if dfs(i, j):
                    cnt += 1
        return cnt