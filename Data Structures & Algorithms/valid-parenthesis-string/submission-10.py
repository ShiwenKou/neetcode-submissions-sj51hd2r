class Solution:
    def checkValidString(self, s: str) -> bool:
        minLeft, maxLeft = 0, 0

        for i in range(len(s)):

            if s[i] == '(':
                minLeft, maxLeft = minLeft + 1, maxLeft + 1

            elif s[i] == ')':
                minLeft, maxLeft = minLeft - 1, maxLeft - 1
            
            else:
                minLeft, maxLeft = minLeft - 1, maxLeft + 1

            if minLeft < 0:
                minLeft = 0
            if maxLeft < 0:
                return False

            

        return minLeft == 0