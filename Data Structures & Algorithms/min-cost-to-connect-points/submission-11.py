class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        



        minHeap = [(0, 0)] # cost, index
        cost = 0
        seen = set()
        while minHeap:

            dist, index = heapq.heappop(minHeap)
            x1, y1 = points[index]
            if index in seen:
                continue
            seen.add(index)
            cost += dist
            
            for i in range(len(points)):
                if i in seen:
                    continue
                
                x2, y2 = points[i]
                d = abs(x1 - x2) + abs(y1 - y2)

                heapq.heappush(minHeap, (d, i))
        return cost