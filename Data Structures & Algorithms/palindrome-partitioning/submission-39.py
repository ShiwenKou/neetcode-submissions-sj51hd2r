class Solution:
    def partition(self, s: str) -> List[List[str]]:
        from functools import cache
        @cache
        def isPali(i, j):
            if i >= j:
                return True
            if s[i] != s[j]:
                return False
            
            res = isPali(i + 1, j - 1)
            return res

        res = []
        sol = []
        def dfs(start):
            if start == len(s):
                res.append(sol[:])
                return
            
            for end in range(start, len(s)):
                if isPali(start, end):

                    sol.append(s[start: end + 1])
                    dfs(end + 1)
                    sol.pop()
        dfs(0)
        return res