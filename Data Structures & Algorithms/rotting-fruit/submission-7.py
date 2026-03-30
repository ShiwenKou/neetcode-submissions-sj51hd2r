class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0
        time = 0
        dq = collections.deque()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    dq.append((r, c))
        
        while dq and fresh > 0:
            length = len(dq)

            for _ in range(length):
                r, c = dq.popleft()

                for nr, nc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nr = r + nr
                    nc = c + nc

                    if (nr not in range(len(grid)) or nc not in range(len(grid[0])) or
                        grid[nr][nc] != 1):
                        continue
                    grid[nr][nc] = 2
                    dq.append((nr, nc))
                    fresh -= 1
            time += 1
        return time if fresh == 0 else -1