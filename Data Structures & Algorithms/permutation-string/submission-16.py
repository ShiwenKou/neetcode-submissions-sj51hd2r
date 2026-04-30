class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        m = len(s1)
        n = len(s2)

        pattern = collections.Counter(s1)
        window = collections.Counter(s2[:m])

        if pattern == window:
            return True
        left = 0
        for right in range(m, n):
            window[s2[right]] += 1

            window[s2[left]] -= 1
            left += 1
            if window[s2[left]] == 0:
                del window[s2[left]]

            if window == pattern:
                return True

        return False