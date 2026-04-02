class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # koko can eat banana within the range of 1 ... max(piles)

        # so we can do binary search on this range, and find the immediate less or equal speed than h

        left, right = 1, max(piles)
        res = max(piles)

        def cal_time(piles, speed):
            time = 0
            for p in piles:
                time += math.ceil(p/speed)
            return time
        while left <= right: # we need to include equal sign here, supposing we have have one element left [1]
            mid = (left + right) // 2

            time = cal_time(piles, mid)

            if time <= h: # mid is a potential valid candidate
                res = min(res, mid) #? check ltr
                right = mid - 1 # eat too fast
            else:
                # time > h. eat too slow
                left = mid + 1
        return res