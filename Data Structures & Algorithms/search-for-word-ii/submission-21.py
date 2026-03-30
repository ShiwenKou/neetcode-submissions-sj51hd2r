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
        for i in range(len(words)):
            root.addWord(words[i])
        res = set()
        sol = []
        seen = set()
        def dfs(r, c, curr):

            if (r not in range(len(board)) or c not in range(len(board[0])) or
                board[r][c] not in curr.children or (r, c) in seen):
                return

            seen.add((r, c)) # need to remove later

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