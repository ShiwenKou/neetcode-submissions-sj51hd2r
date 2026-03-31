class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        sol = []
        def dfs(openn, close):
            if openn == close == n:
                res.append(''.join(sol))
                return
            
            if openn < n:
                sol.append('(')
                dfs(openn + 1, close)
                sol.pop()

            if openn > close:
                sol.append(')')
                dfs(openn, close + 1)
                sol.pop()
        dfs(0, 0)
        return res