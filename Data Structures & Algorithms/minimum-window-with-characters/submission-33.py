class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # once satisfised we shrink right pointer


        pattern = collections.Counter(t)
        window = collections.Counter()
        have, need = 0, len(pattern)

        length = len(s)
        res = ''
        j = 0
        for i in range(len(s)):

            if s[i] in pattern:
                window[s[i]] += 1

                if window[s[i]] == pattern[s[i]]:
                    have += 1

            while have == need:
                if i - j + 1 <= length:
                    res = s[j: i+1]
                    length = i - j + 1
                if s[j] in pattern:
                    window[s[j]] -= 1
                    if window[s[j]] < pattern[s[j]]:
                        have -= 1
                j += 1
        return res

