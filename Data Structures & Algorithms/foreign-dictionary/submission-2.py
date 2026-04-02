class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        
        adjList = {c:set() for w in words for c in w}

        for i in range(len(words) - 1):
            w1 = words[i]
            w2 = words[i + 1]

            minLength = min(len(w1), len(w2))

            if len(w1) > len(w2) and w1[:minLength] == w2[:minLength]:
                return ""
            
            for j in range(minLength):
                c1 = w1[j]
                c2 = w2[j]
                if c1 != c2:
                    adjList[c1].add(c2)
                    break
        seen = set()
        cycle = set()
        res = []
        def dfs(node):

            if node in cycle:
                return False
            if node in seen:
                return True
            
            cycle.add(node)
            for nei in adjList[node]:
                if dfs(nei) == False:
                    return False
            
            cycle.remove(node)
            res.append(node)
            seen.add(node)
            return True
        
        for node in adjList:
            if dfs(node) == False:
                return ""
        res.reverse()
        return ''.join(res)

