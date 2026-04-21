class Solution:
    def isValid(self, s: str) -> bool:
        
        mappings = {']':'[', ')':'(', '}':'{'}

        stack = []
        for i in range(len(s)):

            if s[i] in mappings:


                if stack and stack[-1] == mappings[s[i]]:
                    
                    stack.pop()
                else:
                    return False
            else:
                stack.append(s[i])
        
        return len(stack) == 0