class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        from collections import Counter
        m, n = len(s1), len(s2)
        pattern_freq = Counter(s1)

        window = Counter(s2[:m])
        if pattern_freq == window:
            return True
        for r in range(m, n):
            window[s2[r]] += 1
            window[s2[r-m]] -= 1
            if window[s2[r-m]] == 0:
                del window[s2[r-m]]
            if window == pattern_freq:
                return True
        return False
        