class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        col = set()
        posDiag = set()
        negDiag = set()
        ROWS, COLS = n, n

        board = [['.'] * n for _ in range(n)]
        res = []

        def dfs(r): # r controls the rows
            if r == n:
                copy = [ ''.join(row) for row in board]
                res.append(copy)
                return
            
            for c in range(COLS):
                if ((r + c) in posDiag or (r - c) in negDiag or c in col):
                    continue
                
                posDiag.add((r + c))
                negDiag.add((r - c))
                col.add(c)
                board[r][c] = 'Q'

                dfs(r + 1)
                posDiag.remove((r + c))
                negDiag.remove((r - c))
                col.remove(c)
                board[r][c] = '.'
        dfs(0)
        return res

            

        