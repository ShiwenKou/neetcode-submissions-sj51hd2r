class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        window = collections.Counter()
        res = 0
        left = 0

        for right in range(len(s)):

            window[s[right]] += 1
            while window[s[right]] > 1:
                window[s[left]] -= 1
                if window[s[left]] == 0:
                    del window[s[left]]
                left += 1

            res = max(res, len(window))
        return res
            