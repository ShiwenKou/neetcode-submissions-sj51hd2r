class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        

        cnt = {}

        most_cnt = 0

        left = 0
        res = 0

        for right in range(len(s)):

            cnt[s[right]] = cnt.setdefault(s[right], 0) + 1

            most_cnt = max(most_cnt, cnt.get(s[right], 0))

            if right - left + 1 - most_cnt > k:
                cnt[s[left]] -= 1
                left += 1

            res = max(res, right - left + 1)
        return res