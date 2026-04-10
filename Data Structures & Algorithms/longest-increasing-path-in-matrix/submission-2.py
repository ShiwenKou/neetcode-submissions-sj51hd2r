class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        memo = {}
        def dfs(r, c):

            if (r, c) in memo:
                return memo[(r, c)]
            res = 1
            for nr, nc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr = r + nr
                nc = c + nc
                if (nr not in range(len(matrix)) or nc not in range(len(matrix[0])) or
                    matrix[nr][nc] <= matrix[r][c]):
                    continue
                res = max(res, dfs(nr, nc) + 1)
                memo[(r, c)] = res
            return res
            
        ans = 1
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):

                ans = max(ans, dfs(r, c))
        return ans