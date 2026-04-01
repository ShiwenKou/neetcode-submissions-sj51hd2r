class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        # mappings {pattern:[word]}

        # adjlist

        # bfs
        if endWord not in wordList:
            return 0
        wordList.append(beginWord)
        mappings = collections.defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + '*' + word[i+1:]
                mappings[pattern].append(word)
        
        
        adjList = collections.defaultdict(list)

        for pattern, words in mappings.items():
            for w1 in words:
                for w2 in words:
                    if w1 != w2:
                        adjList[w1].append(w2)      

        dq = collections.deque()
        dq.append(beginWord)
        seen = set()
        seen.add(beginWord)
        res = 1
        while dq:
            for _ in range(len(dq)):
                w = dq.popleft()
                
                if w == endWord:
                    return res
                for nei in adjList[w]:
                    if nei not in seen:
                        dq.append(nei)
                        seen.add(nei)
            res += 1
        return 0

