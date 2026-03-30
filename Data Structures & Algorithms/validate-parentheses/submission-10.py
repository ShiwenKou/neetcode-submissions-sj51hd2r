class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        mappings = {'}':'{', ')':'(',']':'['}
        for i in range(len(s)):
            if s[i] in mappings:
                if not stack:
                    return False

                if mappings[s[i]] != stack[-1]:
                    return False
                stack.pop()
            
            else:
                stack.append(s[i])

        if len(stack) == 0:
            return True
        return False
        