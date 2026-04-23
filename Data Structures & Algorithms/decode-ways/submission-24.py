class Solution:
    def numDecodings(self, s: str) -> int:
        from functools import cache
        @cache
        def dfs(i):
            if i == len(s):
                return 1
            if i > len(s):
                return 0


            res = 0
            sub1 = s[i: i + 1]

            if 1 <= int(sub1) <= 9:
                res += dfs(i + 1)

            sub2 = s[i: i + 2]

            if 10 <= int(sub2) <= 26:
                res += dfs(i + 2)

            return res

        return dfs(0)