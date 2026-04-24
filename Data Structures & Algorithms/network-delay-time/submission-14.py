class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjList = collections.defaultdict(list)
        for n1, n2, time in times:
            adjList[n1].append((time, n2))

        minHeap = [(0, k)]
        seen = set()
        total = 0
        while minHeap:

            cost, node = heapq.heappop(minHeap)
            if node in seen:
                continue
            
            seen.add(node)
            total = cost

            for nei_cost, nei in adjList[node]:
                if nei not in seen:
                    heapq.heappush(minHeap, (cost + nei_cost, nei))
        return total if len(seen) == n else -1


