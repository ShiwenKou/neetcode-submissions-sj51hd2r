class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # when we see minimum, we immediately should consider bfs or it's variant

        # when we see, transform we can use graph.

        # how each words are connected?  -> on position diff, so find out what words r one char diff
        
        if endWord not in wordList:
            return 0
        wordList.append(beginWord)
        mappings = collections.defaultdict(set)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + '*' + word[i + 1:]
                mappings[pattern].add(word) # remove repeatitions
            


        # use bfs here, this is directed graph. we each node has 3 status, so we use two sets to detect cycle
        cycle = set() # visiting nodes in the current path
        seen = set() # visited nodes
        # but seems like the tree status are for dfs
        # so we use seen only for bfs
        dq = collections.deque()
        dq.append(beginWord)
        seen.add(beginWord)
        dist = 1
        while dq:
            length = len(dq) # we want the min, so we use batch here
            
            for _ in range(length):
                curr = dq.popleft()
                if curr == endWord:
                    return dist
                for i in range(len(curr)):
                    pattern = curr[:i] + '*' + curr[i + 1:]
                    for nei in mappings[pattern]:
                        if nei in seen:
                            continue
                        seen.add(nei)
                        dq.append(nei)
            dist += 1
        return 0 # didn't return while bfs

