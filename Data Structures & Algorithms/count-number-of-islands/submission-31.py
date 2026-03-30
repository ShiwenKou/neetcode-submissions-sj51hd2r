class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        total = 0
        seen = set()
        def dfs(r, c):

            if (r not in range(len(grid)) or c not in range(len(grid[0])) or (r, c) in seen or
                grid[r][c] != '1'):
                return

            
            seen.add((r, c))
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)


        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if (r, c) not in seen and grid[r][c] == '1':
                    total += 1
                    dfs(r, c)
        return total
        