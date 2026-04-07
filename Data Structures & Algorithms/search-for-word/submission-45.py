class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        seen = set()

        def dfs(i, r, c):
            if i == len(word):
                return True
            
            if (r not in range(len(board)) or c not in range(len(board[0])) or
                board[r][c] != word[i] or (r, c) in seen):
                return False
            
            seen.add((r, c))

            res = (dfs(i + 1, r + 1, c) or
                   dfs(i + 1, r - 1, c) or
                   dfs(i + 1, r, c + 1) or
                   dfs(i + 1, r, c - 1) 
            ) 

            seen.remove((r, c))

            return res


        for r in range(len(board)):
            for c in range(len(board[0])):

                if dfs(0, r, c):
                    return True
        return False