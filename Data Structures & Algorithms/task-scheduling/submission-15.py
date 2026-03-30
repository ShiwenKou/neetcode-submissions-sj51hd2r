from collections import Counter, deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        maxHeap = list(freq.values())
        
        heapq.heapify_max(maxHeap)

        dq = deque() # pending tasks
        time = 0

        while maxHeap or dq:
            time += 1
            if maxHeap:
                curr = heapq.heappop_max(maxHeap) - 1
                if curr:
                    # add to queque. next time 
                    dq.append([curr, time + n])
            
            if dq:
                if dq[0][1] <= time:
                    pending, _ = dq.popleft()
                    heapq.heappush_max(maxHeap, pending)
        return time



        