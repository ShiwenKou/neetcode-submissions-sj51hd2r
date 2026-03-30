class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False
    def addWord(self, word):
        curr = self
        for i in range(len(word)):
            if word[i] not in curr.children:
                curr.children[word[i]] = TrieNode()
            curr = curr.children[word[i]]
        curr.isEnd = True
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for i in range(len(words)):
            root.addWord(words[i])
        res = set()
        sol = []
        seen = set()
        def dfs(r, c, curr):
            if (r not in range(len(board)) or c not in range(len(board[0])) or (r, c) in seen or
                board[r][c] not in curr.children):
                return
            
            seen.add((r, c))
            sol.append(board[r][c])

            curr = curr.children[board[r][c]]
            if curr.isEnd:
                res.add(''.join(sol))

            dfs(r + 1, c, curr)
            dfs(r - 1, c, curr)
            dfs(r, c + 1, curr)
            dfs(r, c - 1, curr)

            sol.pop()
            seen.remove((r, c))


        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] in root.children:
                    dfs(r, c, root)
        return list(res)