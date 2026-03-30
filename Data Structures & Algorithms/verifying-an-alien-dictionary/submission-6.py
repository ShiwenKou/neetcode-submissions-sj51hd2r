class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:

        mappings = {}

        for i in range(len(order)):
            mappings[order[i]] = i

        for i in range(len(words)-1):
            word1 = words[i]
            word2 = words[i+1]
            for j in range(min(len(word1), len(word2))):

                if mappings[word1[j]] < mappings[word2[j]]:
                    break
                if mappings[word1[j]] > mappings[word2[j]]:
                    return False
            else:
                if len(word1) > len(word2):
                    return False
        return True
        