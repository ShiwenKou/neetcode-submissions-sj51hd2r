class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        mappings = {')':'(', ']':'[', '}':'{'}

        for i in range(len(s)):
            if s[i] in mappings:

                if not stack:
                    return False
                
                if stack[-1] != mappings[s[i]]:
                    return False
                else:
                    stack.pop()

            else:
                stack.append(s[i])
        if len(stack) == 0:
            return True
        else:
            return False
        