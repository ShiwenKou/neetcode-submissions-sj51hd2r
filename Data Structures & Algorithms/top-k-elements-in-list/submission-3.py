class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter

        return list(n for n, f in Counter(nums).most_common(k))
        