class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        lst = []
        res = []
        for x, y in points:
            dist = x**2 + y**2
            lst.append([dist, x, y])
        heapq.heapify(lst)

        while k:
            dist, x, y = heapq.heappop(lst)
            res.append([x,y])
            k -= 1
        return res
