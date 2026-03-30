from collections import Counter, deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        cnt = Counter(tasks)
        cnt = [-v for v in cnt.values()]
        time = 0
        heapq.heapify(cnt)
        dq = deque()
        while cnt or dq:
            time += 1
            if cnt:
                cur = 1 + heapq.heappop(cnt) # current job
                if cur < 0:
                    dq.append([cur, time + n])

            if dq:
                if dq[0][1] <= time :
                    task = dq.popleft()[0]
                    heapq.heappush(cnt, task)
        return time


        