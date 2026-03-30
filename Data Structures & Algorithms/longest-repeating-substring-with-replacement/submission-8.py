class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        from collections import Counter
        res = 0
        left = 0
        window = Counter()
        for right in range(len(s)):
            window[s[right]] += 1
            most_common = window.most_common(1)[0][1]

            while right - left + 1 - most_common > k:

                window[s[left]] -= 1
                if window[s[left]] == 0:
                    del window[s[left]]
                left += 1
            # the above make sure the window is also valid

            res = max(res, right - left + 1)
        return res