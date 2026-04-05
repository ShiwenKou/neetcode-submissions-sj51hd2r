class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        left, right = 1, max(piles)

        def calc_time(piles, speed):
            time = 0

            for p in piles:
                time += math.ceil(p/speed)
            return time

        res = float('inf')
        while left <= right:
            mid = (left + right) // 2

            time = calc_time(piles, mid)

            if time > h: # need to eat faster
                left = mid + 1
            
            else: # need to eat slower, less k
                res = min(mid, res)
                right = mid - 1
        return res
