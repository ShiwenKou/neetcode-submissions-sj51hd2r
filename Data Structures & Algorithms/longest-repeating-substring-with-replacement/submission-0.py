class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        from collections import Counter

        l, r = 0, 0
        window = Counter()
        res = 0
        while r < len(s):

            window[s[r]] += 1
            most_freq = window.most_common(1)[0][1] if window else 0
            while r -l + 1 - most_freq > k:
                window[s[l]] -= 1
                if window[s[l]] == 0:
                    del window[s[l]]
                l += 1
            res = max(res,r-l+1)
            r += 1
        return res