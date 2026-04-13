class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        for i in range(len(points)):

            x, y = points[i]
            dist = x ** 2 + y ** 2
            minHeap.append((dist, x, y))
        
        heapq.heapify(minHeap)
        res = []
        while k:
            d, x, y = heapq.heappop(minHeap)
            res.append([x, y])
            k -= 1
        return res