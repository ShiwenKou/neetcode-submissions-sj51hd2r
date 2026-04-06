class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adjList = {c: set() for word in words for c in word}

        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]

            minLength = min(len(word1), len(word2))
            if len(word1) > len(word2) and word1[:minLength] == word2[:minLength]:
                return ""
            
            for j in range(minLength):
                c1 = word1[j]
                c2 = word2[j]

                if c1 != c2:
                    adjList[c1].add(c2)
                    break

        cycle = set()
        seen = set()
        res = []

        def dfs(node):
            if node in cycle:
                return False
            if node in seen:
                return True
            cycle.add(node)

            for nei in adjList[node]:
                if dfs(nei) == False:
                    return False # a loop detected
            
            seen.add(node)
            res.append(node)
            cycle.remove(node)
            return True
        
        for node in adjList:
            if dfs(node) == False:
                return ''
        
        res.reverse()
        return ''.join(res)