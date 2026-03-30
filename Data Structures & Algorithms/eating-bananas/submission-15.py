class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        res = 0
        left = 1
        right = max(piles)
        def calTime(piles, speed):
            time = 0
            for p in piles:
                time += math.ceil(p/speed)
            return time
        while left <= right:

            mid = (left + right) // 2

            time = calTime(piles, mid)

            if time > h:
                left = mid + 1
            else:
                right = mid - 1
                res = mid
        return res