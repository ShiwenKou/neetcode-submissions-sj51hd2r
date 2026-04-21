class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window = collections.Counter()

        left = 0
        res = 0
        most_cnt = 0
        for right in range(len(s)):
            window[s[right]] += 1
            most_cnt = max(most_cnt, window[s[right]])
            while right - left + 1 - most_cnt  > k:
                window[s[left]] -= 1
                left += 1
            
            res = max(res, right - left + 1)
        return res