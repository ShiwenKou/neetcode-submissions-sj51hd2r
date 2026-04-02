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
                

        
        # no need seen set, cause we will modify the value, and we only visist value = 1
        t = 0
        while dq and fresh > 0:
            length = len(dq)
            for _ in range(length):

                r, c  = dq.popleft()
                
                for nr, nc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nr = r + nr
                    nc = c + nc

                    if (nr not in range(len(grid)) or nc not in range(len(grid[0])) or
                        grid[nr][nc] != 1):
                        continue
                    dq.append((nr, nc))
                    grid[nr][nc] = 2
                    fresh -= 1

            t += 1
        if fresh == 0:
            return t
        else:
            return -1