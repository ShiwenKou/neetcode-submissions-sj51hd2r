class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:



        seen = set()
        def dfs(r, c, i):
            if i == len(word):
                return True
            if (r not in range(len(board)) or c not in range(len(board[0])) or 
                (r, c) in seen or board[r][c] != word[i]):
                return False
            
            
            seen.add((r, c))

            res = (dfs(r + 1, c, i + 1) or dfs(r - 1, c, i + 1) or
                   dfs(r, c + 1, i + 1) or dfs(r, c - 1, i + 1))
            seen.remove((r, c))

            return res

        for r in range(len(board)):
            for c in range(len(board[0])):
                if dfs(r, c, 0):
                    return True
        return False

# O(4^L) where L is the length of word
# O(L)