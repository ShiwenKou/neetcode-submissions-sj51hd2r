class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        dq = collections.deque()
        fresh = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    dq.append((r, c))
                if grid[r][c] == 1:
                    fresh += 1


        time = 0
        while dq and fresh > 0:

            length = len(dq)
            time += 1
            for _ in range(length):
                r, c = dq.popleft()

                for nr, nc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    dr = nr + r
                    dc = nc + c

                    if (dr not in range(len(grid)) or dc not in range(len(grid[0])) or
                        grid[dr][dc] != 1):
                        continue
                    dq.append((dr, dc))
                    grid[dr][dc] = 2
                    fresh -= 1
        return time if fresh == 0 else -1