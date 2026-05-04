class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        window = {}
        most_common = 0
        length = 0
        left = 0
        for right in range(len(s)):
            window[s[right]] = window.setdefault(s[right], 0) + 1
            most_common = max(most_common, window[s[right]])

            if right - left + 1 - most_common  > k:
                window[s[left]] -= 1
                left += 1
            
            length = max(length, right - left + 1)
        return length

