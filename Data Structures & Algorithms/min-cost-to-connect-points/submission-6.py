class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # use bfs, each time we go the neartest to the current node
        # maintain a minHeap, we can start anywhere
        adjList = collections.defaultdict(list)
        for i in range(len(points)):
            for j in range(len(points)):
                if i != j:
                    x1, y1 = points[i]
                    x2, y2 = points[j]
                    dist = abs(x1 - x2) + abs(y1 - y2)
                    adjList[i].append([dist, j])

        minHeap = [[0, 0]]
        seen = set()
        cost = 0
        while minHeap:

            curr_dist, curr = heapq.heappop(minHeap)
            if curr in seen:
                continue # curr has been processed and added to cost
            seen.add(curr)
            cost += curr_dist

            for nei_dist, nei in adjList[curr]:
                
                heapq.heappush(minHeap, [nei_dist, nei])
        return cost
