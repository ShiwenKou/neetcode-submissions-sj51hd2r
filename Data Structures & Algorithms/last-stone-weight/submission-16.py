class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        lst = [-c for c in stones]
        heapq.heapify(lst)

        while len(lst) > 1:
            stone1 = -heapq.heappop(lst)
            stone2 = -heapq.heappop(lst)

            if stone1 > stone2:
                heapq.heappush(lst, -(stone1 - stone2))
        lst.append(0)
        res = -lst[0]
        return res

        