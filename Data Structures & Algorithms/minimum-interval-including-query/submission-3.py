class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        
        minHeap = []

        intervals.sort()
        i = 0
        res = {}
        for q in sorted(queries):
            while i < len(intervals) and intervals[i][0] <= q: # current interals[i] is a potentials for current q
                start, end = intervals[i]
                heapq.heappush(minHeap, (end - start + 1, end) ) # we want the minimum interval for q. we also want to maintain the minHeap
                # we use end to maintain a good minHeap such that the current minHeap also contains potential intervals for q
                i += 1
            while minHeap and minHeap[0][1] < q: # we need to pop this intervals, tho it is shorted but not good for current q
                heapq.heappop(minHeap)

            res[q] = minHeap[0][0] if minHeap else -1 # sometimes q may in the right of all the potentials(in other words on potential intervals for current q. according to the problem statement we have to return -1)
            # the q are interated in sorted order, but we need to return the original order so we use a hashmap to track that
        return list(res[q] for q in queries)
