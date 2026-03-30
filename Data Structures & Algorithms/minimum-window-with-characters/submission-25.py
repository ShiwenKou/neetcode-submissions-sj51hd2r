class Solution:
    def minWindow(self, s: str, t: str) -> str:

        pattern = collections.Counter(t)
        window = collections.Counter()

        res = ''
        have = 0
        need = len(pattern)
        length = float('inf')
        left = 0
        for right in range(len(s)):

            if s[right] in pattern:
                window[s[right]] += 1

                if window[s[right]] == pattern[s[right]]:
                    have += 1

            while have == need:
                if right - left + 1 < length:
                    res = s[left: right + 1]
                    length = min(length, right - left + 1)

                if s[left] in pattern:
                    window[s[left]] -= 1
                    if window[s[left]] < pattern[s[left]]:
                        have -= 1
                left += 1
        return res
        