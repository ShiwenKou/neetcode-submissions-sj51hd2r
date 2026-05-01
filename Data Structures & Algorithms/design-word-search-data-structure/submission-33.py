class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.end = True

    def search(self, word: str) -> bool:


        def dfs(j, curr):
            for i in range(j, len(word)):

                if word[i] == '.': # backtracking
                    # we have 26 potention solutions

                    for child in curr.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False

                else:

                    if word[i] not in curr.children:
                        return False
                    
                    curr = curr.children[word[i]]

            return curr.end     

        return dfs(0, self.root)   
