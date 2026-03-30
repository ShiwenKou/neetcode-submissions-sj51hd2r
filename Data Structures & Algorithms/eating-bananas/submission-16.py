class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        res = 0
        left = 1
        right = max(piles)
        def calTime(piles, speed):
            t = 0

            for p in piles:
                t += math.ceil(p/speed)
            return t
        while left <= right:
            mid = (left + right) // 2

            time = calTime(piles, mid)

            if time > h:
                left = mid + 1
            else:
                res = mid
                right = mid - 1
        return res
        