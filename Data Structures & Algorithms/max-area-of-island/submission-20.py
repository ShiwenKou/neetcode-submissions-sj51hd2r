class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        

        def dfs(r, c):

            if (r not in range(len(grid)) or c not in range(len(grid[0])) or grid[r][c] != 1):
                return 0

            grid[r][c] = 0

            res = 1 + dfs(r + 1, c) +  + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)
            return res

        res = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] != 1:
                    continue
                res = max(res, dfs(r, c))
        return res