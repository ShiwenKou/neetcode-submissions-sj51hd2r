class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        

        total = 0
        seen = set()
        def bfs(r, c):

            dq = collections.deque()
            dq.append((r, c))
            seen.add((r, c))

            while dq:
                r, c = dq.popleft()

                for nr, nc in [(1,0), (-1,0), (0, 1), (0, -1)]:
                    nr = nr + r
                    nc = nc + c

                    if (nr not in range(len(grid)) or nc not in range(len(grid[0])) or
                        (nr, nc) in seen or grid[nr][nc] != '1'):
                        continue
                    
                    dq.append((nr, nc))
                    seen.add((nr, nc))


        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if (r, c) not in seen and grid[r][c] == '1':
                    total += 1
                    bfs(r, c)

        return total