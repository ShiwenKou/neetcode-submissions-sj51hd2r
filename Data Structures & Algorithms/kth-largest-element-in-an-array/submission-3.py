class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        lst = [-v for v in nums]
        heapq.heapify(lst)

        while k:
            res = heapq.heappop(lst)
            k -= 1
        return -res