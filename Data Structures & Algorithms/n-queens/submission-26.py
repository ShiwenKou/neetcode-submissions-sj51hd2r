class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        posDiag = set()
        cols = set()
        negDiag = set()

        board = [['.'] * n for _ in range(n)]
        res = []
        def dfs(r):

            if r == n:
                copy = list(''.join(row) for row in board)
                res.append(copy)

            
            for c in range(n):

                if (c in cols or (r + c) in posDiag or (r - c) in negDiag):
                    continue

                
                cols.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)

                board[r][c] = 'Q'

                dfs(r + 1)

                board[r][c] = '.'
                posDiag.remove(r + c)
                negDiag.remove(r - c)
                cols.remove(c)

        dfs(0)
        return res