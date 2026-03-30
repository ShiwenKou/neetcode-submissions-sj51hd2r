from collections import Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        freq = Counter(tasks)
        maxHeap = list(v for v in freq.values())
        heapq.heapify_max(maxHeap)

        dq = deque()
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
        