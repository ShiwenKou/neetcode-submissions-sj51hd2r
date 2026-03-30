class Solution:
    def isPalindrome(self, s: str) -> bool:

        l, r = 0, len(s) - 1

        while l < r: # looking for pairs

            while l < r and  not s[l].isalnum():
                l += 1
                # continue
            while l < r and not s[r].isalnum():
                r -= 1
                # continue
            

            if s[l].lower() == s[r].lower():
                l += 1
                r -= 1
            else:
                return False
        return True

        