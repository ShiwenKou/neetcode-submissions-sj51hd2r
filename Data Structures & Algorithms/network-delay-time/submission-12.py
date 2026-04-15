class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        

        adjList = collections.defaultdict(list)

        for n1, n2, cost in times:
            adjList[n1].append((cost, n2))
        
        minHeap = [(0, k)]


        seen = set()
        total = 0
        while minHeap:

            cost, node = heapq.heappop(minHeap)
            if node in seen:
                continue
            seen.add(node)
            total = max(cost, total)
            for nei_time, nei in adjList[node]:

                heapq.heappush(minHeap, (nei_time + cost, nei))
        return total if len(seen) == n else -1
