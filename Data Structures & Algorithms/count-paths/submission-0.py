class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        memo = {}
        def dfs(r, c):

            if r == m - 1 and c == n - 1:
                return 1
            
            if (r, c) in memo:
                return memo[(r, c)]
            res = 0
            for nr, nc in [(1, 0), (0, 1)]:
                nr = nr + r
                nc = nc + c

                if (nr not in range(m) or nc not in range(n)):
                    continue
                res += dfs(nr, nc)
            
            memo[(r, c)] = res
            return res

        return dfs(0, 0)
                


            
            
