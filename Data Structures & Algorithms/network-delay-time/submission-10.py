class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjList = collections.defaultdict(list)
        for n1, n2, t in times:
            adjList[n1].append((t, n2))

        minHeap = [(0, k)]
        seen = set()
        total = 0
        while minHeap:

            t, curr = heapq.heappop(minHeap)
            if curr in seen:
                continue
            total = max(total, t)
            seen.add(curr)

            for nei_time, nei in adjList[curr]:
                if nei not in seen: #(optimize)
                    heapq.heappush(minHeap, (t + nei_time, nei))
        return total if len(seen) == n else -1
        