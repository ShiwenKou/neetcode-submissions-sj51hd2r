class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxHeap = [-c for c in nums]

        heapq.heapify(maxHeap)

        while k:
            res = heapq.heappop(maxHeap)
            k -= 1
        return -res
        