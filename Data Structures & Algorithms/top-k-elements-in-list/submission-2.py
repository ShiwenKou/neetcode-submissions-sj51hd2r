class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        from collections import Counter

        return list(v for v, f in Counter(nums).most_common(k))
        