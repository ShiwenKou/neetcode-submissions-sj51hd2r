class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjList = collections.defaultdict(list)
        for n1, n2, time in times:
            adjList[n1].append((n2, time))
        
        minHeap = [(0, k)]

        seen = set()
        while minHeap:

            t, curr = heapq.heappop(minHeap)
            if curr in seen:
                continue

            seen.add(curr)

            res = t
            for nei, nei_time in adjList[curr]:
                # if nei not in seen:
                heapq.heappush(minHeap, (t + nei_time, nei))
        

        return res if len(seen) == n else -1
