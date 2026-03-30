class Solution:
    def longestPalindrome(self, s: str) -> str:


        ans = ""

        lenans = 0
        center = 0

        for center in range(len(s)):
            left = center
            right = center

            while left >= 0 and right < len(s) and s[left] == s[right]:

                if right - left + 1 > lenans:
                    ans = s[left: right + 1]
                    lenans = len(ans)
                
                left -= 1
                right += 1
            

            left = center
            right = center + 1

            while left >= 0 and right < len(s) and s[left] == s[right]:

                if right - left + 1 > lenans:
                    ans = s[left: right + 1]
                    lenans = len(ans)
                
                left -= 1
                right += 1
            
        return ans




        