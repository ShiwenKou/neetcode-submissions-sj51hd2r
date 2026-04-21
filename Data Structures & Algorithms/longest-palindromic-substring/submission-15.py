class Solution:
    def longestPalindrome(self, s: str) -> str:
        from functools import cache

        @cache
        def dfs(i, j):

            if i >= j:
                return True
            
            if s[i] != s[j]:
                return False
            
            res = dfs(i + 1, j - 1)

            return res
        length = 0
        res = ''
        for i in range(len(s)):
            for j in range(i, len(s)):

                if dfs(i, j):
                    if j - i + 1 > length:
                        res = s[i: j+ 1]
                        length = j - i + 1
        return res
