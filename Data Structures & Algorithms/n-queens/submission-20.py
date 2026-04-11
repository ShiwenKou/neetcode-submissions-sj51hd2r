class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        

        posDiag = set()
        negDiag = set()
        cols = set()
        board = [['.'] * n for _ in range(n)]
        res = []
        def dfs(r):

            if r == n:
                copy = [''.join(row) for row in board]
                res.append(copy)

            for c in range(n):
                if ( c in cols or (r + c) in posDiag or (r - c) in negDiag):
                    continue
                cols.add(c)
                posDiag.add(c + r)
                negDiag.add(r - c)
                board[r][c] = 'Q'

                dfs(r + 1)

                cols.discard(c)
                posDiag.discard(c + r)
                negDiag.discard(r - c)
                board[r][c] = '.'
        dfs(0)
        return res





