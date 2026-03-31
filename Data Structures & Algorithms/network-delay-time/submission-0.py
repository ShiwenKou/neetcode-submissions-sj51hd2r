class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjList = collections.defaultdict(list)
        for u, v, t in times:
            adjList[u].append([v, t])
        
        minHeap = [(0, k)]
        seen = set()
        t = 0
        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in seen:
                continue
            seen.add(n1)
            t = w1

            for n2, w2 in adjList[n1]:
                if n2 not in seen:
                    heapq.heappush(minHeap,(w1+w2,n2))
        return t if len(seen) == n else -1

            