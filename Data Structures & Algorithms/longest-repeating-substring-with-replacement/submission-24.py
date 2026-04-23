class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window = {}

        max_common = 0
        left = 0
        res = 0
        for right in range(len(s)):

            window[s[right]] = 1 + window.get(s[right], 0)

            max_common = max(max_common, window[s[right]])

            while right - left + 1 - max_common > k:
                window[s[left]] -= 1
                left += 1
            res = max(res, right - left + 1)
        return res