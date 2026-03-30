class Solution:
    def countSubstrings(self, s: str) -> int:

        ans = 0
        center = 0
        for center in range(len(s)):

            left = center
            right = center

            while left >= 0 and right < len(s) and s[left] == s[right]:
                ans += 1
                left -= 1
                right += 1
            
            left = center
            right = center + 1

            while left >= 0 and right < len(s) and s[left] == s[right]:
                ans += 1
                left -= 1
                right += 1
        return ans
            


        