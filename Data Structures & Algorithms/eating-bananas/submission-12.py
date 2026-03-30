class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        # this problem we need to interate from 1 to max(piles) to find a minimum k, that taketime(k) <= h

        # we can brute force iterate the range from 1 to max(piles), however, we can actually use a binary search
        # which will minimize the time complexity for big O of N* max(piles) to big O of n * log max(piles)

        left, right = 1, max(piles) - 1
        res = max(piles)
        while left <= right: # actually we want to find a target that help(k) <=h

            mid = (left + right) // 2

            taketime = self.help(piles, mid)

            
            if taketime <= h:
                res = min(res, mid)
                # we need larger k
                right = mid - 1

            else: # taketime <= h
                
                left = mid + 1
        return res

    def help(self, piles, mid):
        t = 0
        for i in piles:

            t += math.ceil(i/mid)
        return t
        