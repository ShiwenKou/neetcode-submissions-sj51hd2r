class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        adjList = collections.defaultdict(list)
        for n1, n2, t in times:
            adjList[n1].append((t, n2))
        minHeap = [(0, k)]

        seen = set()
        cost = 0
        while minHeap:

            t, node = heapq.heappop(minHeap)

            if node in seen:
                continue
            
            seen.add(node)
            cost = t
            for t_nei, nei in adjList[node]:
                if nei not in seen: # optimization

                    heapq.heappush(minHeap, (t_nei + t, nei))
        if len(seen) == n:
            return cost
        else:
            return -1