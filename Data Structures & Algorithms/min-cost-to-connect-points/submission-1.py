class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adjList = collections.defaultdict(list)
        for i in range(len(points)):
            x1, x2 = points[i]
            for j in range(len(points)):
                if j == i:
                    continue
                y1, y2 = points[j]
                dist = abs(x1 - y1) + abs(x2 - y2)
                adjList[i].append([dist, j])
                adjList[j].append([dist, i])
                
        seen = set()
        minHeap = [[0,1]]
        cost = 0
        while len(seen) < len(points):
        
            dist, node = heapq.heappop(minHeap)
            if node in seen:
                continue
            seen.add(node)
            cost += dist

            for nei_dist, nei in adjList[node]:
                if nei not in seen:
                    heapq.heappush(minHeap, [nei_dist, nei])
        return cost
