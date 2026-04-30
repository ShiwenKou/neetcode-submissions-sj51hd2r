class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        
        # each pass have a maximum, we want the minimum among those maximums.
        # this is because the maximums are the bottleneck


        
        minHeap = [(grid[0][0], 0, 0)]



        seen = set()


        while minHeap:

            cost, r, c = heapq.heappop(minHeap)

            if (r, c) in seen:
                continue
            seen.add((r, c))
            if r == c == len(grid) - 1:
                return cost

            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr = r + dr
                nc = c + dc

                if (nr not in range(len(grid)) or nc not in range(len(grid[0])) or
                    (nr, nc) in seen):
                    continue
                heapq.heappush(minHeap, (max(cost, grid[nr][nc]), nr, nc))
