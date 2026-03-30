class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        from collections import Counter
        res = 0
        l = 0
        window = Counter()

        for r in range(len(s)):
            window[s[r]] += 1
            most_common = window.most_common(1)[0][1]

            while r - l + 1 - most_common > k:
                window[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)
        return res


        