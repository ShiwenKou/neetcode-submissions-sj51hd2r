from collections import Counter
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window = Counter()
        left = 0
        length = 0
        for right in range(len(s)):
            window[s[right]] += 1
            most_common = window.most_common(1)[0][1]

            while right - left + 1 - most_common > k:
                window[s[left]] -= 1
                left += 1
            length = max(length, right - left + 1)
        return length



        