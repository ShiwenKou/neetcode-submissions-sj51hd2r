class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        
        minHeap = [(grid[0][0], 0, 0)]

        seen = set()
        seen.add((0, 0))

        while minHeap: # when we use minHeap, we cannot use batch bfs

            height, r, c = heapq.heappop(minHeap)

            if r == c == len(grid) - 1:
                return height
            for nr, nc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr = r + nr
                nc = c + nc

                if (nr not in range(len(grid)) or nc not in range(len(grid[0])) or
                    (nr, nc) in seen):
                    continue
                
                heapq.heappush(minHeap, (max(grid[nr][nc], height), nr, nc))
                seen.add((nr, nc))

