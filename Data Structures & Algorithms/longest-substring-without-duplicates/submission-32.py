class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = collections.Counter()
        left = 0
        res = 0
        for right in range(len(s)):

            window[s[right]] += 1

            while window[s[right]] > 1:
                window[s[left]] -= 1
                left += 1
            res = max(res, right - left + 1)
        return res
            



        