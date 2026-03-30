class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxHeap = [-v for v in nums]
        heapq.heapify(maxHeap)

        while k > 0:
            res = heapq.heappop(maxHeap)
            k -= 1
        return -res
        