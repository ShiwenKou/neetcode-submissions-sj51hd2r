class Solution:
    def isValid(self, s: str) -> bool:

        mappings = {"]":"[",")":"(","}":"{"}
        stack = []

        for c in s:
            if c in mappings:
                if stack[-1] == mappings[c] if stack else None:
                    stack.pop()
                else:
                    return False

            else:
                stack.append(c)
        if len(stack) == 0:
            return True
        else:
            return False