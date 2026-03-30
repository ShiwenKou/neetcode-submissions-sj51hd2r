class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False
    def addWord(self, word):
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.end = True
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()

        for w in words:
            root.addWord(w)
        res = set()
        seen = set()
        sol = []
        def dfs(r, c, curr):
            if (r not in range(len(board)) or c not in range(len(board[0])) or (r, c) in seen or
                board[r][c] not in curr.children):
                return
            
            seen.add((r, c))
            sol.append(board[r][c])

            curr = curr.children[board[r][c]]
            if curr.end:
                res.add(''.join(sol))
            
            dfs(r + 1, c, curr)
            dfs(r - 1, c, curr)
            dfs(r, c + 1, curr)
            dfs(r, c - 1, curr)

            sol.pop()
            seen.remove((r, c))
        

        for r in range(len(board)):
            for c in range(len(board[0])):
                dfs(r, c, root)
        return list(res)