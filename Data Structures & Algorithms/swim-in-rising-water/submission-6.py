class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        

        minHeap = [(grid[0][0], 0, 0)] # cost r, c


        seen = set()
        minn = 0
        while minHeap:

            cost, r, c = heapq.heappop(minHeap)
            if (r, c) in seen:
                continue
            seen.add((r, c))
            if r == c == len(grid) - 1:
                return cost
            for nr, nc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                nr = r + nr
                nc = c + nc

                if (nr not in range(len(grid)) or nc not in range(len(grid[0])) or (nr, nc) in seen):
                    continue
                
                heapq.heappush(minHeap, (max(grid[nr][nc], cost), nr, nc))
        
        return minn