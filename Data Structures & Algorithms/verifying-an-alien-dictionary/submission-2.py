class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:

        mappings = {v:i for i, v in enumerate(order)}


        for i in range(len(words)-1):

            w1 = words[i] 
            w2 = words[i+1] # word2


            # comparing char by char

            for j in range(min(len(w1),len(w2))):

                c1 = w1[j] # char from word1
                c2 = w2[j] # char from word2

                if mappings[c1] > mappings[c2]:
                    return False
                if mappings[c1] < mappings[c2]:
                    break # this pair of words pass
            
            else:
                if len(w1) > len(w2):
                    return False
        return True
        