class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        seen = set()

        def dfs(r, c):
            if (r not in range(len(grid)) or c not in range(len(grid[0])) or 
                grid[r][c] != 1 or (r, c) in seen):
                return 0

            seen.add((r, c))

            res = 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)

            return res
        ans = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if (r, c) not in seen and grid[r][c] == 1:
                    ans = max(ans, dfs(r, c))
        return ans

# 每个格子只看了一次，所以是 O(m*n)
# 空间复杂度主要看的是 recursion depth and seen set: worst case O(m*n) 最坏从(0,0)一直recursion到 (m-1,n-1) 。或者 每个格子都是1