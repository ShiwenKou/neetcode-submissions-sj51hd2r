class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        
        adjList = {char:set() for word in words for char in word}

        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]
            minLength = min(len(word1), len(word2))

            if len(word1) > len(word2) and word1[:minLength] == word2[:minLength]:
                return ''

            for j in range(minLength):
                char1 = word1[j]
                char2 = word2[j]
                if char1 != char2:
                    adjList[char1].add(char2)
                    break

        cycle = set()
        seen = set()
        res = []
        def dfs(word):
            if word in cycle:
                return False
            if word in seen:
                return True

            cycle.add(word)

            for nei in adjList[word]:
                if not dfs(nei):
                    return False

            cycle.remove(word)
            res.append(word)
            seen.add(word)
            return True

        for word in adjList:
            if not dfs(word):
                return ''
        
        res.reverse()

        return ''.join(res)
            
