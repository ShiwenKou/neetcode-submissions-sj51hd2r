class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        from collections import Counter
        import heapq

        counter = Counter(nums) # num : freq

        heap = []

        for num, freq in counter.items():

            heapq.heappush(heap, (freq, num))

            if len(heap) > k:
                heapq.heappop(heap)
        
        return list(num for freq, num in heap)

        