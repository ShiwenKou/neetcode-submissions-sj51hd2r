class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adjList = collections.defaultdict(list)
        for i in range(len(points)):
            for j in range(len(points)):
                if i != j:
                    x1, y1 = points[i]
                    x2, y2 = points[j]
                    dist = abs(x1 - x2) + abs(y1 - y2)
                    adjList[i].append([dist, j])
        
        seen = set()

        minHeap = [[0, 0]] # dist, node
        cost = 0
        while minHeap:

            dist, node = heapq.heappop(minHeap)
            if node in seen:
                continue
            seen.add(node)
            cost += dist
            for nei_dist, nei in adjList[node]:
                if nei in seen:
                    continue
                
                heapq.heappush(minHeap, [nei_dist, nei])
        return cost