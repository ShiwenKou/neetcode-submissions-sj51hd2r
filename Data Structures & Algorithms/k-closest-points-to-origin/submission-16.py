class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        # we need a minHeap

        minHeap = [(p1**2 + p2**2, p1, p2) for p1, p2 in points]
        heapq.heapify(minHeap)
        res = []
        while k:

            _, p1, p2 = heapq.heappop(minHeap)
            res.append([p1, p2])
            k -= 1
        return res