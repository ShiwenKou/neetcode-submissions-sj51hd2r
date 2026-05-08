class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        
        good = set()
        for p in triplets:
            if p[0] > target[0] or p[1] > target[1] or p[2] > target[2]:
                continue

            for i, v in enumerate(p):

                if v == target[i]:
                    good.add(i)
        return len(good) == 3