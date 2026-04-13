class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adjList = collections.defaultdict(list)
        for i in range(len(points)):
            for j in range(len(points)):
                if i != j:
                    x1, y1 = points[i]
                    x2, y2 = points[j]
                    dist = abs(x1 - x2) + abs(y1 - y2)
                    adjList[i].append((dist, j))

        res = 0
        minHeap = [(0, 0)]
        seen = set()
        while minHeap:
            
            dist, node = heapq.heappop(minHeap)

            if node in seen:
                continue
            
            seen.add(node)
            res += dist

            for nei_dist, nei in adjList[node]:
                if nei not in seen:
                    heapq.heappush(minHeap, (nei_dist, nei))
        return res