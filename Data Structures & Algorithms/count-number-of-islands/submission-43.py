class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        from collections import deque

        dq = deque()


        def bfs():

            while dq:
                length = len(dq)
                for _ in range(length):
                    r, c = dq.popleft()
                    grid[r][c] = '0'

                    for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                        nr = dr + r
                        nc = dc + c
                        if (nr not in range(len(grid)) or nc not in range(len(grid[0])) or
                            grid[nr][nc] != '1'):
                            continue
                        dq.append((nr, nc))
                    
            

        total = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):

                if grid[r][c] == '1':
                    total += 1
                    dq.append((r, c))
                    bfs()

        return total