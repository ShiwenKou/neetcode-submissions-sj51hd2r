class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # the pattern behind this problem is to use seen set mark every '1'

        seen = set()
        
        def bfs(r, c):
            
            dq = collections.deque()
            dq.append((r, c))
            
            while dq:
                r, c = dq.popleft()

                for nr, nc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nr = r + nr
                    nc = c + nc
                    if (nr not in range(len(grid)) or nc not in range(len(grid[0])) or
                        (nr, nc) in seen or grid[nr][nc] != '1'):
                        continue
                    dq.append((nr, nc))
                    seen.add((nr, nc))
        

        total = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '1' and (r, c) not in seen:
                    seen.add((r, c))
                    total += 1
                    bfs(r, c)
        return total
