class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        from collections import Counter
        if len(s) == 0:
            return ''
        pattern_freq = Counter(t)
        window = Counter()
        have, need = 0, len(pattern_freq)
        l = 0
        res = [-1, -1]
        length = float('inf')
        for r in range(len(s)):
            window[s[r]] += 1
            if s[r] in pattern_freq and pattern_freq[s[r]] == window[s[r]]:
                have += 1
        
            while have == need:
                if r - l + 1 < length:
                    res = [l, r]
                    length = r - l + 1

                window[s[l]] -= 1
                if pattern_freq[s[l]] > window[s[l]]:
                    have -= 1
                l += 1
        return s[res[0]:res[1]+1]