from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROWS = defaultdict(set)
        COLS = defaultdict(set)
        SQUARES = defaultdict(set)

        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == '.':
                    continue
                if (board[i][j] in ROWS[i] or
                   board[i][j] in COLS[j] or
                   board[i][j] in SQUARES[(i//3, j//3)]):
                   return False
                
                ROWS[i].add(board[i][j])
                COLS[j].add(board[i][j])
                SQUARES[(i//3, j//3)].add(board[i][j])
        return True
        