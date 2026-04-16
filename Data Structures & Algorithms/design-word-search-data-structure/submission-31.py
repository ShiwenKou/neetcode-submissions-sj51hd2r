class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
    def addWord(self, word: str) -> None:
        cur = self.root
        for i in range(len(word)):
            if word[i] not in cur.children:
                cur.children[word[i]] = TrieNode()
            cur = cur.children[word[i]]
        cur.end = True
        

    def search(self, word: str) -> bool:

        def dfs(start, cur):
            for i in range(start, len(word)):
                if word[i] == '.':
                    # We have 26 potential paths to go
                    for child in cur.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                
                else:
                    if word[i] not in cur.children:
                        return False
                    cur = cur.children[word[i]]
            
            return cur.end # for循环结束，如果没有return False就可以return True/False

        return dfs(0, self.root)

        
