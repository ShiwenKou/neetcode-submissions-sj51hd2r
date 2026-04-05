class Solution:
    def numDecodings(self, s: str) -> int:
        
        memo = {}
        def dfs(start):
            if start == len(s):
                return 1
            if start in memo:
                return memo[start]
            res = 0
            
            if s[start: start + 1] != '0':
                res += dfs(start + 1)
            
            if start + 1 < len(s) and 10 <= int(s[start: start + 2]) <= 26:
                res += dfs(start + 2)
            
            memo[start] = res
            return res

        return dfs(0)
        