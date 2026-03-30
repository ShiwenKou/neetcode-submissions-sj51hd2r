class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        from collections import Counter

        counter = Counter(nums)

        import heapq


        heap = []


        for num, freq in counter.items():
            heapq.heappush(heap,(freq,num))

            if len(heap) > k:
                heapq.heappop(heap)
        return [num for freq, num in heap]
        