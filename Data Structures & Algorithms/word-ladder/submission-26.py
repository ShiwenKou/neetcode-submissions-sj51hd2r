class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        wordList.append(beginWord)
        mappings = collections.defaultdict(set)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + '*' + word[i + 1:]
                mappings[pattern].add(word)

        seen = set()

        dq = collections.deque()
        dq.append(beginWord)
        seen.add(beginWord)

        res = 0
        while dq:
            length = len(dq)
            res += 1
            for _ in range(length):
                node = dq.popleft()
                
                if node == endWord:
                    return res
                for i in range(len(node)):
                    pattern = node[:i] + '*' + node[i + 1:]
                    for nei in mappings[pattern]:
                        if nei not in seen:
                            dq.append(nei)
                            seen.add(nei)
        return 0
\