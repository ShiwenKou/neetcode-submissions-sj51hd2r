class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        


        total = 0
        rows = len(grid)
        cols = len(grid[0])
        seen = set()

        def bfs(r, c):
            dq = collections.deque()
            dq.append((r, c))
            seen.add((r, c))

            while dq:
                r, c = dq.popleft()
                for nr, nc in [(1,0),(-1,0),(0,1),(0,-1)]:
                    nr = r + nr
                    nc = c + nc

                    if nr not in range(rows) or nc not in range(cols) or grid[nr][nc] != '1' or (nr, nc) in seen:
                        continue
                    else:
                        seen.add((nr, nc))
                        dq.append((nr, nc))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r, c) not in seen:
                    total += 1
                    bfs(r, c)
        return total