from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m, n = len(s1), len(s2)
        pattern = Counter(s1)
        window = Counter(s2[:m])
        if pattern == window:
            return True

        for right in range(m, n):
            window[s2[right]] += 1
            window[s2[right - m]] -= 1
            if window[s2[right - m]] == 0:
                del window[s2[right - m]]
            if window == pattern:
                return True
        return False

        