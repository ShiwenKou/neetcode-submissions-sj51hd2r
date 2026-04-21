class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        counter = {}

        for n in nums:
            counter[n] = 1 + counter.get(n, 0)

        res = []
        # from 0 freq to max_freq we can have a new array

        mappings = [[] for _ in range(len(nums) + 1)]

        for n, freq in counter.items():
            mappings[freq].append(n)
        
        for i in range(len(mappings) - 1, 0, -1):

            if mappings[i]:
                for n in mappings[i]:
                    res.append(n)
                    if len(res) == k:
                        return res