class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        from collections import Counter
        m, n = len(s1), len(s2)
        freq1 = Counter(s1)

        window = Counter(s2[:m])

        if freq1 == window:
            return True

        for i in range(m, n):

            window[s2[i]] += 1
            window[s2[i - m]] -= 1

            if window[s2[i - m]] == 0:
                del window[s2[i - m]]
            if freq1 == window:
                return True
        return False
        