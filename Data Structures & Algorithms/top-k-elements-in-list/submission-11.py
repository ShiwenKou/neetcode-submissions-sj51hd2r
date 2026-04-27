class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        counter = {}
        bucket = [[] for _ in range(len(nums) + 1)]
        res = []
        for n in nums:
            counter[n] = 1 + counter.get(n, 0)

        for n, freq in counter.items():
            bucket[freq].append(n)

        for i in range(len(bucket) - 1, 0, -1):

            if bucket[i]:

                for n in bucket[i]:
                    res.append(n)
                    if len(res) == k:
                        return res

        
