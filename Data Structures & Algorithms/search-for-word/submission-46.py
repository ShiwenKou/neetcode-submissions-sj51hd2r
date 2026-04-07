class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        seen = set()
 
        def dfs(i, r, c):
            if i == len(word):
                return True
            seen.add((r, c))

            for nr, nc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr = r + nr
                nc = c + nc
                if (nr not in range(len(board)) or nc not in range(len(board[0])) or
                    board[nr][nc] != word[i] or (nr, nc) in seen):
                    continue

                if dfs(i + 1, nr, nc):
                    return True

            seen.remove((r, c))



        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == word[0]:
                    if dfs(1, r, c):
                        return True
        return False