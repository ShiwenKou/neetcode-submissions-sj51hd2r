class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adjList = {char: set() for word in words for char in word}
        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]

            minLength = min(len(word1), len(word2))

            if word1[:minLength] == word2[:minLength] and len(word1) > len(word2):
                return ''
            for j in range(minLength):
                c1 = word1[j]
                c2 = word2[j]
                if c1 != c2:
                    adjList[c1].add(c2)
                    break
            
        # topological sort and reverse?

        res = []

        cycle = set()
        seen = set()
        def dfs(node):
            if node in cycle:
                return False
            if node in seen:
                return True
            cycle.add(node)

            for nei in adjList.get(node,[]):
                if not dfs(nei): # a loop detected, there is not relative order
                    return False

            cycle.remove(node)
            seen.add(node)
            res.append(node)
            return True

        for node in adjList:
            if not dfs(node):
                return ''
        res.reverse()
        return ''.join(res)

