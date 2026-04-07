class Solution:
    def countSubstrings(self, s: str) -> int:
        

        res = 0


        for ctr in range(len(s)):

            left, right = ctr, ctr

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