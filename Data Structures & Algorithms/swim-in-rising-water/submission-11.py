class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # we are looking for the minimum from the maximum level down differnt path


        minHeap = [(grid[0][0], 0, 0)]
        seen = set()
        while minHeap:

            prev_level, r, c = heapq.heappop(minHeap)
            if (r, c) in seen:
                continue
            
            seen.add((r, c))
            if r == c == len(grid) - 1:
                return prev_level

            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr = dr + r
                nc = dc + c

                if (nr not in range(len(grid)) or nc not in range(len(grid[0])) or (nr, nc) in seen):
                    continue
                
                heapq.heappush(minHeap, (max(prev_level, grid[nr][nc]), nr, nc))
        
