from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:

        window = Counter()
        pattern = Counter(t)

        left = 0
        have, need = 0, len(pattern)
        minRes = float('inf')
        res = [-1, -1]
        for i in range(len(s)):

            if s[i] in pattern:
                window[s[i]] += 1
                if window[s[i]] == pattern[s[i]]:
                    have += 1
            
            while have == need:
                if i - left + 1 < minRes:
                    res = [left, i + 1]
                    minRes = i - left + 1
                if s[left] in pattern:
                    window[s[left]] -= 1
                    if window[s[left]] < pattern[s[left]]:
                        have -= 1
                left += 1
        return s[res[0]:res[1]]
        