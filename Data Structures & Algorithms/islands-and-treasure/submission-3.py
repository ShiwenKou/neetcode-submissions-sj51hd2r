class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:


        dq = collections.deque()
        seen = set()

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    dq.append((r, c))
                    seen.add((r, c))
        dist = 0
        while dq:
            length = len(dq)
            for _ in range(length):

                r, c = dq.popleft()
                grid[r][c] = dist
                for nr, nc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nr = nr + r
                    nc = nc + c
                    if (nr not in range(len(grid)) or nc not in range(len(grid[0])) or
                        (nr, nc) in seen or grid[nr][nc] == -1):
                        continue
                    dq.append((nr, nc))
                    seen.add((nr, nc))
            dist += 1