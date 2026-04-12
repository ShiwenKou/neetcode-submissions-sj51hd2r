class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        lst = collections.Counter(tasks)

        dq = collections.deque()

        maxHeap = [freq for freq in lst.values()]
        heapq.heapify_max(maxHeap)
        time = 0
        while maxHeap or dq:
            time += 1
            if maxHeap:
                cur  = heapq.heappop_max(maxHeap) - 1
                if cur:
                    dq.append((time + n, cur))

            if dq:

                if dq[0][0] <= time:
                    _, pending = dq.popleft()
                    heapq.heappush_max(maxHeap, pending)
        
        return time