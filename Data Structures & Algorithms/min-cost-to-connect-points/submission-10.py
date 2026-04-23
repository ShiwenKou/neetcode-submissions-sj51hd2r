class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        # adjList = collections.defaultdict(list)
        # for p1 in points:
        #     for p2 in points:
        #         if p1 != p2:
        #             x1, y1 = p1
        #             x2, y2 = p2
        #             dist = abs(x1 - x2) + abs(y1 - y2)
        #             adjList[p1].append(dist, x2, y2)

        x1, y1 = points[0]
        minHeap = [(0,x1,y1)]
        seen = set()
        cost = 0
        while minHeap:

            dist, x1, y1 = heapq.heappop(minHeap)

            if (x1, y1) in seen:
                continue
            seen.add((x1, y1))
            cost += dist
            for x2, y2 in points:
                if (x2, y2) not in seen:
                    d = abs(x1 - x2) + abs(y1 - y2)
                    heapq.heappush(minHeap, (d, x2, y2))
        return cost


                
