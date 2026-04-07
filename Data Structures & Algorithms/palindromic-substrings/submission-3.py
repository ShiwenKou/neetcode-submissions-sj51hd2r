class Solution:
    def countSubstrings(self, s: str) -> int:
        res = len(s)
        for ctr in range(len(s)):

            # odd

            left, right = ctr - 1, ctr + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:

                res += 1

                left -= 1
                right += 1

            left, right = ctr, ctr + 1

            while left >= 0 and right < len(s) and s[left] == s[right]:
                res += 1

                left -= 1
                right += 1
        return res



            # even