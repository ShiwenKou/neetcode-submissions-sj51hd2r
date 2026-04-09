class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        curr = self.root

        for i in range(len(word)):
            if word[i] not in curr.children:
                curr.children[word[i]] = TrieNode()
            curr = curr.children[word[i]]
        curr.end = True
        

    def search(self, word: str) -> bool:

        def dfs(start, curr):
            for i in range(start, len(word)):
                if word[i] == '.':
                    # potential 26 new path to explore
                    for child in curr.children.values():
                        if dfs(i + 1, child) == True:
                            return True
                    return False
                
                else:
                    if word[i] not in curr.children:
                        return False
                    curr = curr.children[word[i]]
            
            return curr.end
        
        return dfs(0, self.root)
            
