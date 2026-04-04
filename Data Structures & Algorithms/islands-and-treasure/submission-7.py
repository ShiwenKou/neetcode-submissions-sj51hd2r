class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        dq = collections.deque()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    dq.append((r, c))
        
        dist = 0
        seen = set()
        while dq:
            length = len(dq)
            for _ in range(length):
                r, c = dq.popleft()
                grid[r][c] = dist
                seen.add((r, c))
                for nr, nc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nr = r + nr
                    nc = c + nc

                    if (nr not in range(len(grid)) or nc not in range(len(grid[0])) or
                        grid[nr][nc] == -1 or (nr, nc) in seen):
                        continue
                    dq.append((nr, nc))
                    seen.add((nr, nc))
            dist += 1