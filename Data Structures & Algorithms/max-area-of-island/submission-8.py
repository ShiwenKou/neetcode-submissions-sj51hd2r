class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        seen = set()
        res = 0

        def dfs(r, c):
            # our target is to add 1's to seen

            if (r not in range(len(grid)) or c not in range(len(grid[0])) or (r, c) in seen or
                grid[r][c] != 1):
                return 0
            
            seen.add((r, c))

            return (1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1))


        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1 and (r, c) not in seen:
                    res = max(res, dfs(r, c))
        return res