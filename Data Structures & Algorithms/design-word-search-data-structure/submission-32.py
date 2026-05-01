class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.end = True

    def search(self, word: str) -> bool:

        

        def dfs(j, curr):
            for i in range(j, len(word)):

                if word[i] == '.':
                    # we have up to 26 potention solutions

                    for child in curr.children.values(): # curr.children contains all potention keys/solutions at the current Trie Tree layer
                        # we do backtracking here

                        if dfs(i + 1, child):
                            return True
                    # Tried all solutions in curr.children
                    return False
                
                else:

                    if word[i] not in curr.children:
                        return False
                    curr = curr.children[word[i]]
            return curr.end

        return dfs(0, self.root)
