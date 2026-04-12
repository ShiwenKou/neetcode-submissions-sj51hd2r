class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        memo = [[-1] * (n + 1) for _ in range(m + 1)]
        
        def dfs(r, c):
            if c == n:
                return 1
            if r == m:
                return 0
            if memo[r][c] != -1:
                return memo[r][c]
            
            res = 0
            for i in range(r, m):
                if s[i] == t[c]:
                    res += dfs(i + 1, c + 1)
            memo[r][c] = res
            return res
        
        return dfs(0, 0)