class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        

        minHeap = [(grid[0][0], 0, 0)] # time, grid(r, c)



        seen = set()

        while minHeap:

            cost, r, c = heapq.heappop(minHeap)

            if (r, c) in seen:
                continue # if we alr find a minumum for (r, c), we'd skip
            seen.add((r, c))
            if r == c == len(grid) - 1:
                return cost
            for nr, nc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr = nr + r
                nc = nc + c

                if (nr not in range(len(grid)) or nc not in range(len(grid[0])) or
                    (nr, nc) in seen):
                    continue
                
                heapq.heappush(minHeap, (max(grid[nr][nc], cost), nr, nc))
        
        