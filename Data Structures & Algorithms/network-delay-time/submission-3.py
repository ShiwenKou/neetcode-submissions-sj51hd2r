class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        adjList = collections.defaultdict(list)

        for n1, n2, time in times:
            adjList[n1].append((n2, time))

        seen = {}
        minHeap = [(0, k)]

        while minHeap:
            curr_time, curr = heapq.heappop(minHeap)

            if curr in seen:
                continue
            
            seen[curr] = curr_time

            for nei, nei_time in adjList[curr]:
                if nei not in adjList[curr]:
                    heapq.heappush(minHeap, (nei_time + curr_time, nei))
        
        return max(seen.values()) if len(seen) == n else -1