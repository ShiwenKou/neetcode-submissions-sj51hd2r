class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        
        counter = collections.Counter(hand)
        minHeap = list(counter.keys())
        heapq.heapify(minHeap)
        while minHeap:

            first = minHeap[0]

            for i in range(first, first + groupSize):
                if i not in counter:
                    return False # not consecutive anymore return False
                
                counter[i] -= 1

                
                if counter[i] == 0:
                    if i != minHeap[0]:
                        return False # a hole exist return False
                    heapq.heappop(minHeap)

        return True