class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        adjList = collections.defaultdict(list)

        for n1, n2, t in times:
            adjList[n1].append([n2, t])

        minHeap = [(0, k)]

        seen = set()
        t = 0
        while minHeap:
            curr_time, curr = heapq.heappop(minHeap)

            if curr in seen:
                continue
            seen.add(curr)
            t = max(curr_time, t)

            for nei, nei_time in adjList[curr]:
                if nei not in seen:
                    heapq.heappush(minHeap, (t + nei_time, nei))
        return t if len(seen) == n else -1