class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter
        pattern = Counter(t)
        window = Counter()
        have, need = 0, len(pattern)
        left = 0
        res = [-1, -1]
        length = float('inf')
        for right in range(len(s)):
            if s[right] in pattern:
                window[s[right]] += 1
                if window[s[right]] == pattern[s[right]]:
                    have += 1

            while have == need:

                if right - left + 1 < length:
                    res = [left, right]
                    length = right - left + 1

                if s[left] in pattern:
                    window[s[left]] -= 1
                    if window[s[left]] < pattern[s[left]]:
                        have -= 1
                left += 1
        return s[res[0]: res[1]+1]
                