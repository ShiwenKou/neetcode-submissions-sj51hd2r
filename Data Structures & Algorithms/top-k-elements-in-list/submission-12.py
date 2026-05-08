class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        

        counter = {}
        res = [[] for _ in range(len(nums) + 1)]
        ans = []
        for n in nums:
            counter[n] = counter.get(n, 0) + 1
        
        for n, freq in counter.items():

            res[freq].append(n)

        
        for i in range(len(res) - 1, -1, -1):

            if res[i]:
                
                for n in res[i]:
                    ans.append(n)
                    if len(ans) == k:
                        return ans

