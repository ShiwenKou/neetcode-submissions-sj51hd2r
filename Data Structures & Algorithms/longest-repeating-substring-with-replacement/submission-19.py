class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        window = collections.Counter()
        left = 0
        res = 0
        most_common = 0
        for right in range(len(s)):

            window[s[right]] += 1
            most_common = max(most_common, window[s[right]])
            # length - most_common <= k

            while right - left + 1 - most_common > k:
                window[s[left]] -= 1

                if window[s[left]] == 0:
                    del window[s[left]]
                left += 1
            
            res = max(res, right - left + 1)
        return res