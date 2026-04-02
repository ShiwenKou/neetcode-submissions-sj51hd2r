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
        for word in words:
            root.add(word)
        
        seen = set()
        res = set()
        sol = []
        def dfs(r, c, curr):
            

            if (r not in range(len(board)) or c not in range(len(board[0])) or
                board[r][c] not in curr.children or (r, c) in seen):
                return
            
            sol.append(board[r][c])
            seen.add((r, c))

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