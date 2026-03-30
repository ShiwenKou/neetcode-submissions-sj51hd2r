class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        counter = [0] * 26

        for i in range(len(s)):
            counter[ord(s[i])- ord('a')] += 1

        for i in range(len(t)):
            counter[ord(t[i])- ord('a')] -= 1

            if counter[ord(t[i])- ord('a')] < 0:
                return False
        
        return True