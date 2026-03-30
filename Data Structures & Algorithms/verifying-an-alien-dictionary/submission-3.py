class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:

        mappings = {w:i for i, w in enumerate(order)}


        # comparing two words
        # get their char at index j
        # if check failed return False
        # if check ok break check if it is a substring
        

        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i+1]

            for j in range(min(len(word1), len(word2))):
                c1 = word1[j]
                c2 = word2[j]

                if mappings[c1] > mappings[c2]:
                    return False
                if mappings[c1] < mappings[c2]:
                    break

            else:

                if len(word1) > len(word2):
                    return False
        return True


        