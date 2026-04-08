class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjList = collections.defaultdict(list)
        for n1, n2, t in times:
            adjList[n1].append((t, n2))

        minHeap = [(0, k)]


        seen = set()
        t = 0
        while minHeap:

            node_t, node = heapq.heappop(minHeap)

            if node in seen:
                continue
            
            seen.add(node)
            t = max(t, node_t)

            for nei_t, nei in adjList[node]:
                if nei not in seen:
                    heapq.heappush(minHeap, (nei_t + node_t, nei))
        if len(seen) == n:
            return t
        else:
            return -1