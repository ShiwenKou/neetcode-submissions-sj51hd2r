class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        adjList = collections.defaultdict(list)
        for n1, n2, t in times:
            adjList[n1].append((t, n2))

        
        minHeap = [(0, k)]
        seen = set()
        total = 0
        while minHeap:

            time, node = heapq.heappop(minHeap)

            if node in seen:
                continue
            seen.add(node)

            total = max(time, total)

            for nei_t, nei in adjList[node]:
                if nei not in seen:
                    heapq.heappush(minHeap, (nei_t + time, nei))

        return total if len(seen) == n else -1