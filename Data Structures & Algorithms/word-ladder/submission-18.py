class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        wordList.append(beginWord)
        mappings = collections.defaultdict(list)

        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i + 1:]
                mappings[pattern].append(word)

        # this feels like a undirected graph
        res = []
        sol = []
        seen = set()

        dq = collections.deque()
        dq.append(beginWord)
        res = 0
        while dq:
            length = len(dq)
            res += 1
            for _ in range(length): # we need to count the steps so we use a for loop here
                word = dq.popleft()
                seen.add(word)
                if word == endWord:
                    return res

                for i in range(len(word)):
                    pattern = word[:i] + "*" + word[i + 1:]
                    for nei in mappings[pattern]:
                        if nei not in seen: # this is like the base case
                            dq.append(nei)
                            seen.add(nei)
        return 0

            
