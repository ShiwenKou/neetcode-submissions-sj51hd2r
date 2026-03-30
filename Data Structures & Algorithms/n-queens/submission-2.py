class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        res = []
        # sol = []

        col = set()
        posDiagonal = set() # r + c
        negDiagonal = set() # r - c

        board = [['.'] * n for _ in range(n)]

        def dfs(r):
            if r == n:
                copy = [''.join(row) for row in board]
                res.append(copy)        
                return
            
            for c in range(len(board[0])):
                if (c in col or (r - c) in negDiagonal or (r + c) in posDiagonal):
                    continue
                
                col.add(c)
                posDiagonal.add(r+c)
                negDiagonal.add(r-c)
                board[r][c] = 'Q'

                dfs(r + 1)
                col.remove(c)
                posDiagonal.remove(r+c)
                negDiagonal.remove(r-c)
                board[r][c] = '.'
        dfs(0)
        return res
