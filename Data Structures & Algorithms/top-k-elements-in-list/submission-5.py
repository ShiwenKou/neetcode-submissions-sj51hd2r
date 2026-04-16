class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
         
        counter = {}

        freq = [[] for _ in range(len(nums) + 1)]
        res = []
        for n in nums:
            counter[n] = 1 + counter.get(n, 0)
        
        for n, f in counter.items():
            freq[f].append(n)

        for i in range(len(freq) - 1, 0, -1):
            if freq[i]:
                for n in freq[i]:
                    res.append(n)

            
                    if k == len(res):
                        return res


