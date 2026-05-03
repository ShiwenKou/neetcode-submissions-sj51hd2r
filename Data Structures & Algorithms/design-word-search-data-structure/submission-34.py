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
        curr = self.root

        def dfs(j, curr):
            for i in range(j, len(word)):

                if word[i] == '.':
                    for child in curr.children.values():
                        if dfs(i + 1, child):
                            return True

                    return False
                else:

                    if word[i] not in curr.children:
                        return False
                    
                    curr = curr.children[word[i]]
            return curr.end
        
        return dfs(0, curr)
