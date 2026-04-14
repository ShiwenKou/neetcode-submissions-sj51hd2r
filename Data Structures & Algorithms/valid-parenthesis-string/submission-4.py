class Solution:
    def checkValidString(self, s: str) -> bool:
        
        from functools import cache
        @cache


        def dfs(i, openn):

            if i == len(s):
                return openn == 0
            if openn < 0:
                return False
            
            if s[i] == '(':
                res = dfs(i + 1, openn + 1)
            elif s[i] == ')':
                res = dfs(i + 1, openn - 1)
            if s[i] == '*':
                # three options
                res = (dfs(i + 1, openn + 1) or
                       dfs(i + 1, openn) or
                       dfs(i + 1, openn - 1))

            return res
        return dfs(0, 0)