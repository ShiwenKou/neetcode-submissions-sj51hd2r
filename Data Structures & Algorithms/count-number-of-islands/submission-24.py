class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        

        dq = collections.deque()
        total = 0
        seen = set()
        def bfs(r, c):

            dq.append((r, c))

            while dq:
                r, c = dq.popleft()
                seen.add((r, c))

                for nr, nc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nr = r + nr
                    nc = c + nc

                    if (nr not in range(len(grid)) or nc not in range(len(grid[0])) or
                        (nr, nc) in seen or grid[nr][nc] != '1'):
                        continue
                    seen.add((nr, nc))
                    dq.append((nr, nc))



        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if (r, c) not in seen and grid[r][c] == '1':
                    bfs(r, c)
                    total += 1

        return total