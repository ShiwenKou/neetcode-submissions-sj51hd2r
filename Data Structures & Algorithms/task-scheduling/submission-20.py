class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        freq = collections.Counter(tasks)
        maxHeap = list(freq.values())
        dq = collections.deque()
        heapq.heapify_max(maxHeap)
        time = 0
        while maxHeap or dq:
            time += 1

            if maxHeap:
                curr = heapq.heappop_max(maxHeap) - 1
                if curr:
                    dq.append([curr, time + n])
            if dq:
                if dq[0][1] <= time:
                    pending, _ = dq.popleft()
                    heapq.heappush_max(maxHeap, pending)

        return time