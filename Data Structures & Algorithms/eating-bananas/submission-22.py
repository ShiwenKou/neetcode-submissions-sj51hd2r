class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def calc_time(speed, piles):
            time = 0
            for p in piles:
                time += math.ceil(p / speed)
            return time


        left, right = 1, max(piles)
        res = max(piles)
        while left <= right:

            mid = (left + right) // 2

            time = calc_time(mid, piles)

            if time <= h: # eat ok. but can you eat slower?
                res = min(mid, res)

                right = mid - 1

            else:
                left = mid + 1
        return res
