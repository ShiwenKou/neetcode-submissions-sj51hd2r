class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        minHeap = [[x**2 + y**2, x, y] for x, y in points ]

        heapq.heapify(minHeap)

        res = []

        while k:
            _, x, y = heapq.heappop(minHeap)
            res.append([x, y])
            k -= 1
        return res


        