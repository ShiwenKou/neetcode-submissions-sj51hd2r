class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = list(-c for c in stones)
        heapq.heapify(heap)

        while len(heap) >= 2:
            stone1 = heapq.heappop(heap) * - 1
            stone2 = heapq.heappop(heap) * - 1

            if stone1 > stone2:
                heapq.heappush(heap, stone2 - stone1)
            elif stone1 < stone2:
                heapq.heappush(heap, stone1 - stone2)
        
        if len(heap) == 1:
            return -heap[0]
        elif len(heap) == 0:
            return 0