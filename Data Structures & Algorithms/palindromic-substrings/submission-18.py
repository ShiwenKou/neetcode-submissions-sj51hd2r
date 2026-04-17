class Solution:
    def countSubstrings(self, s: str) -> int:
        
        cnt = 0
        for ctr in range(len(s)):


            left = ctr
            right = ctr
            while left >= 0 and right < len(s) and s[left] == s[right]:
                cnt += 1
                left -= 1
                right += 1
            
            left = ctr
            right = ctr + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                cnt += 1
                left -= 1
                right += 1
        return cnt
