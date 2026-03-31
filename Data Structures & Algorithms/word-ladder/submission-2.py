class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        nei = collections.defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + '*' + word[j + 1:]
                nei[pattern].append(word)
        adjList = collections.defaultdict(set)
        for pattern, word in nei.items():
            for w1 in word:
                for w2 in word:
                    if w1 != w2:
                        adjList[w1].add(w2)

        dq = collections.deque()
        dq.append(beginWord)
        seen = set()
        seen.add(beginWord)
        res = 1

        while dq:
            for _ in range(len(dq)):
                curr = dq.popleft()
                seen.add(curr)
                if curr == endWord:
                    return res
                for nei in adjList[curr]:
                    if nei not in seen:
                        dq.append(nei)
            res += 1
        return 0
