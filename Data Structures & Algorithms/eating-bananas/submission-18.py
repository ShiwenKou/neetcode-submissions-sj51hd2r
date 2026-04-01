class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        res = right
        def calc_t(piles, mid):
            time = 0
            for p in piles:
                time += math.ceil(p/mid)
            return time
        while left <= right:
            mid = (left + right) // 2

            time = calc_t(piles, mid)

            if time <= h: # eat too fast, but a candidate

                res = min(res, mid)
                right = mid - 1
            else:
                left = mid + 1
        return res