class Solution:
    def numDecodings(self, s: str) -> int:
        
        from functools import cache
        @cache
        def dfs(start):
            if start == len(s):
                return 1
            
            res = 0
            sub1 = s[start: start + 1]
            if 0 < int(sub1) <= 9:
                res += dfs(start + 1)
            
            if start + 2 <= len(s):
                sub2 = s[start: start + 2]

                if sub2[0] != '0' and 10 <= int(sub2) <= 26:
                    res += dfs(start + 2)
            return res
        return dfs(0)