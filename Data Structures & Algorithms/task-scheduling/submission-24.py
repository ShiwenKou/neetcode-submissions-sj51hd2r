class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cnt = collections.Counter(tasks)

        maxHeap = [v for v in cnt.values()]
        heapq.heapify_max(maxHeap)

        dq = collections.deque() # for pending tasks

        time = 0

        while maxHeap or dq:
            time += 1

            if maxHeap:
                curr = heapq.heappop_max(maxHeap) - 1 # processed, so minus one
                if curr: # not 0. append them to dq
                    dq.append((curr, time + n))

            if dq:
                if dq[0][1] <= time:
                    pending, _ = dq.popleft()
                    heapq.heappush_max(maxHeap, pending)
        return time