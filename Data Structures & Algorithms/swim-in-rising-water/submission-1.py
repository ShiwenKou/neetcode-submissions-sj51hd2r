class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        

        minHeap = [(grid[0][0], 0, 0)] # [r, c]

        seen = set()
        while minHeap:

            height, r, c = heapq.heappop(minHeap)

            seen.add((r, c))

            if r == c == len(grid) - 1:
                return height
            for nr, nc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr = r + nr
                nc = c + nc
                if (nr not in range(len(grid)) or nc not in range(len(grid[0]))
                    or (nr, nc) in seen):
                    continue
                seen.add((nr, nc))
                heapq.heappush(minHeap, (max(height, grid[nr][nc]), nr, nc))