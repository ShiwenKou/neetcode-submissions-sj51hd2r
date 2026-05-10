class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        
        intervals.sort()
        # we need to maintain a minHeap to collection all potential intervals for current queries


        minHeap = []
        i = 0
        res = {}
        for q in sorted(queries):

            while i <= len(intervals) - 1 and intervals[i][0] <= q:
                start, end = intervals[i][0], intervals[i][1]
                heapq.heappush(minHeap, (end - start + 1, end)) # this end index is used to filter out or pushpop minheap for maintainance
                i += 1
            
            while minHeap and minHeap[0][1] < q:
                heapq.heappop(minHeap) # pop those intervals that are not fit for current q

            # then minHeap[0] is the best interval for current q

            res[q] = minHeap[0][0] if minHeap else -1

        return list(res[q] for q in queries)
 
