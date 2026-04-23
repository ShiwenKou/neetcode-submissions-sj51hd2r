class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        counter = collections.Counter(nums)

        mapping = [[] for _ in range(len(nums) + 1)]


        for num, freq in counter.items():
            mapping[freq].append(num)

        
        
        for i in range(len(mapping) - 1, 0, -1):
            if mapping[i]:
                for n in mapping[i]:
                    res.append(n)

                    if len(res) == k:
                        return res