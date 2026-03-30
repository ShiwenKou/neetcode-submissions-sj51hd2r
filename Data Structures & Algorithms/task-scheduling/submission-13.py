from collections import Counter, deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        time = 0
        freq = Counter(tasks)
        maxHeap = [-v for v in freq.values()]
        heapq.heapify(maxHeap)
        dq = deque()

        while maxHeap or dq:

            time += 1

            if maxHeap:
                task = heapq.heappop(maxHeap) + 1
                if task:
                    dq.append([task, time + n])

            if dq:
                if dq[0][1] <= time:
                    pending, _ = dq.popleft()
                    heapq.heappush(maxHeap, pending)

        return time
        