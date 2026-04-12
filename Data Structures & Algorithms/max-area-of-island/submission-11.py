class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        

        seen = set()

        def dfs(r, c):
            if (r not in range(len(grid)) or c not in range(len(grid[0])) or
                grid[r][c] != 1 or (r, c) in seen):
                    return 0
            
            seen.add((r, c))
                
            return (1 + dfs(r + 1, c)
             + dfs(r - 1, c)
             + dfs(r, c + 1)
             + dfs(r, c - 1))

            

            return res



        total = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1 and (r, c) not in seen:
                    total = max(dfs(r, c), total)

        return total