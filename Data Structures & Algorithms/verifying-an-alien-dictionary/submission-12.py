class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        mappings = {}
        for i, v in enumerate(order):
            mappings[v] = i
        
        for i in range(len(words) - 1):
            w1 = words[i]
            w2 = words[i + 1]

            for j in range(min(len(w1), len(w2))):
                c1 = w1[j]
                c2 = w2[j]


                if mappings[c1] < mappings[c2]:
                    break
                
                if mappings[c1] > mappings[c2]:
                    return False
            else:
                if len(w1) > len(w2):
                    return False
        return True
