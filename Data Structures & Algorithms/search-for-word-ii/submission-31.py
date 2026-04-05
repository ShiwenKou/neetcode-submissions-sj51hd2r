class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False
    
    def addWord(self, word):
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
            root.addWord(word)

        res = set()
        seen = set()
        sol = []
        def dfs(r, c, node):

            if (r not in range(len(board)) or c not in range(len(board[0])) or
                (r, c) in seen or board[r][c] not in node.children):
                return
            seen.add((r, c))

            curr = node.children[board[r][c]]
            sol.append(board[r][c])

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
                if board[r][c] in root.children: # redundant cuz in the dfs we'll check again
                    dfs(r, c, root)
        return list(res)
