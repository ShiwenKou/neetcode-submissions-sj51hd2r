class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        total = 0
        seen = set()
        dq = collections.deque()
        def bfs(r, c):

            dq.append((r, c))

            while dq:
                length = len(dq)
                for _ in range(length):
                    r, c = dq.popleft()
                    seen.add((r, c))
                    for nr, nc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                        nr = r + nr
                        nc = c + nc
                        if (nr not in range(len(grid)) or nc not in range(len(grid[0])) or
                            grid[nr][nc] != '1' or (nr, nc) in seen):
                            continue
                        dq.append((nr, nc))



        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if (grid[r][c] == '1' and (r, c) not in seen):
                    total += 1
                    bfs(r, c)
        return total