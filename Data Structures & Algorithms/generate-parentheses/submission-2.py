class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        ans, curr = [], []
        def dfs(openn, close):

            if len(curr) == 2*n:
                ans.append(''.join(curr))
                return
            if openn < n:
                curr.append('(')
                dfs(openn+1, close)
                curr.pop()

            if openn > close:
                curr.append(')')
                dfs(openn, close + 1)
                curr.pop()
            return
        dfs(0, 0)
        return ans
        