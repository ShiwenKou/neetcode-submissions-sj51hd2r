class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        right = max(piles)
        left = 1
        res = right
        def getTime(piles, mid):
            time = 0
            for p in piles:
                time += math.ceil(p/ mid)
            return time

        while left <= right:
            mid = (left + right) // 2

            time = getTime(piles, mid)

            if time <= h:
                res = mid
                right = mid - 1

            else:
                left = mid + 1
        return res