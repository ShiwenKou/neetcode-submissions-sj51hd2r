class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # graph problem
        # add to wordList

        # building pattern

        if endWord not in wordList:
            return 0
        
        wordList.append(beginWord)
        mappings = collections.defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + '*' + word[i + 1:]
                mappings[pattern].append(word)
        # bfs
        dq = collections.deque()
        dq.append(beginWord)
        seen = set()
        seen.add(beginWord)
        dist = 1
        while dq:
            length = len(dq)
            for _ in range(length):
                word = dq.popleft()
                if word == endWord:
                    return dist
                seen.add(word)

                for i in range(len(word)):
                    pattern = word[:i] + '*' + word[i + 1:]
                    for nei in mappings[pattern]:
                        if nei in seen:
                            continue
                        dq.append(nei)
                        seen.add(nei)
            dist += 1
        return 0

