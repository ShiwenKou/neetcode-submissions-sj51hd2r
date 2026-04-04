class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        wordList.append(beginWord)
        mappings = collections.defaultdict(list)

        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + '*' + word[i+1:]
                mappings[pattern].append(word)

        dq = collections.deque()

        dq.append(beginWord)
        dist = 0
        seen = set()
        while dq:
            length = len(dq)
            dist += 1
            for _ in range(length):
                word = dq.popleft()
                if word == endWord:
                    return dist
                
                seen.add(word)
                for i in range(len(word)):
                    pattern = word[:i] + '*' + word[i+1:]
                    for nei in mappings[pattern]:
                        if nei not in seen:
                            dq.append(nei)
        return 0