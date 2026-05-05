class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        cnt = collections.Counter(tasks)
        maxHeap = list(cnt.values())

        heapq.heapify_max(maxHeap)

        dq = collections.deque()
        time = 0
        while maxHeap or dq:
            time += 1
            if maxHeap:
                cur = heapq.heappop_max(maxHeap) - 1
                if cur:
                    dq.append((cur, time + n))

            if dq:
                if dq[0][1] <= time:
                    pending, _ = dq.popleft()
                    heapq.heappush_max(maxHeap, pending)

        return time