class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        length = 0
        res = ''
        for ctr in range(len(s)):


            left = right = ctr

            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > length:
                    res = s[left: right + 1]
                    length = right - left + 1
                
                left -= 1
                right += 1

            left = ctr
            right = ctr + 1

            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > length:
                    res = s[left: right + 1]
                    length = right - left + 1
                
                left -= 1
                right += 1
        return res