class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False
    def add(self, word):
        curr = self
        for i in range(len(word)):
            if word[i] not in curr.children:
                curr.children[word[i]] = TrieNode()
            curr = curr.children[word[i]]
        curr.end = True
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        root = TrieNode()
        for i in range(len(words)):
            root.add(words[i])
        sol = []
        res = set()
        seen = set()
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


            seen.remove((r, c))
            sol.pop()

        for r in range(len(board)):
            for c in range(len(board[0])):
                dfs(r, c, root)
        return list(res)

        