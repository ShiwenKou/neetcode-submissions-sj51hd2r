class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        mapping = {}
        for i, v in enumerate(order):
            mapping[v] = i

        for i in range(len(words) - 1):

            word1 = words[i]
            word2 = words[i + 1]


            for j in range(min(len(word1), len(word2))):

                char1 = word1[j]
                char2 = word2[j]

                if mapping[char1] < mapping[char2]:
                    break
                elif mapping[char1] > mapping[char2]:
                    return False
            else:
                if len(word1) > len(word2):
                    return False

        return True
                


        