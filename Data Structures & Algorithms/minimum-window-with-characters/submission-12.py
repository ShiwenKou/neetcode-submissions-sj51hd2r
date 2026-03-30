class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter

        pattern = Counter(t)
        window = Counter()
        have, need = 0, len(pattern)
        length = float('inf')
        left = 0
        res = [-1, -1]
        for i in range(len(s)):
            if s[i] in pattern:
                window[s[i]] += 1
                if window[s[i]] == pattern[s[i]]:
                    have += 1
            
            while have == need:

                if i - left + 1 < length:
                    res = [left, i]
                    length = min(length, i - left + 1)

                if s[left] in pattern:
                    window[s[left]] -= 1
                    if window[s[left]] < pattern[s[left]]:
                        have -= 1
                left += 1
        return s[res[0]: res[1]+1]


        