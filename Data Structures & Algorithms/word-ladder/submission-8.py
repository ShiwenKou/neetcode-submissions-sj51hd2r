class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        wordList.append(beginWord)
        mappings = collections.defaultdict(list)
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + '*' + word[j+1:]
                mappings[pattern].append(word)
        
        dq = collections.deque()
        dq.append(beginWord)
        seen = set()
        seen.add(beginWord)
        res = 1
        while dq:
            length = len(dq)
            for _ in range(length):
                word = dq.popleft()

                if word == endWord:
                    return res
                
                for j in range(len(word)):
                    pattern = word[:j] + '*' + word[j+1:]
                    for nei in mappings[pattern]:
                        if nei not in seen:
                            dq.append(nei)
                            seen.add(nei)
            
            res += 1
        return 0