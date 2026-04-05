class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        mappings = collections.defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + '*' + word[i + 1:]
                mappings[pattern].append(word)
        
        dist = 0
        dq = collections.deque()
        dq.append(beginWord)
        # bfs for minimum path, unweighted graph
        seen = set()
        seen.add(beginWord)
        while dq:

            length = len(dq)
            dist += 1
            for _ in range(length):

                word = dq.popleft()
                
                if word == endWord:
                    return dist

                for i in range(len(word)):
                    pattern = word[:i] + '*' + word[i + 1:]
                    for nei in mappings[pattern]:
                        if nei not in seen:
                            dq.append(nei)
                            seen.add(nei)
        return 0
