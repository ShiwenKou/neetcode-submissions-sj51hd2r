class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        mappings = {']':'[',')':'(','}':'{'}

        for c in s:

            if c in mappings:
                if not stack:
                    return False
                if mappings[c] != stack[-1]:
                    return False
                stack.pop()
            else:
                stack.append(c)
        
        if len(stack) == 0:
            return True
        else:
            return False