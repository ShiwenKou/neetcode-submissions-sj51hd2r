class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        # left = 1, right = max(piles)

        left = 1
        right = max(piles)
        res = 0
        def calc_time(speed, piles):
            time = 0
            for p in piles:
                time += math.ceil(p / speed)
            return time
        while left <= right:

            mid = (left + right) // 2

            time = calc_time(mid, piles)

            if time <= h:
                res = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return res