class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        adjList = collections.defaultdict(list)
        for n1, n2, time in times:
            adjList[n1].append([n2, time])
        
        minHeap = [[0, k]]

        total = 0

        seen = set()

        while minHeap:

            t, node = heapq.heappop(minHeap)
            if node in seen:
                continue
            total = t
            seen.add(node)

            for nei, nei_time in adjList[node]:
                if nei not in seen:
                    heapq.heappush(minHeap, [t + nei_time, nei])
        return total if len(seen) == n else -1