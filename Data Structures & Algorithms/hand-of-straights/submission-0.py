class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        count = collections.Counter(hand)
        minHeap = [k for k in count.keys()]
        heapq.heapify(minHeap)

        while minHeap:
            first = minHeap[0]

            for i in range(first, groupSize + first):
                if i not in count:
                    return False
                count[i] -= 1

                if count[i] == 0:
                    if minHeap[0] != i:
                        return False
                    heapq.heappop(minHeap)
        return True