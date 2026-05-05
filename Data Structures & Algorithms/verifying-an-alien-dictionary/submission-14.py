class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        mappings = {}
        for i, char in enumerate(order):
            mappings[char] = i
        
        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]

            minLength = min(len(word1), len(word2))

            for j in range(minLength):

                char1 = word1[j]
                char2 = word2[j]

                if mappings[char1] > mappings[char2]:
                    return False
                if mappings[char1] < mappings[char2]:
                    break
            else:
                if len(word1) > len(word2):
                    return False
        return True