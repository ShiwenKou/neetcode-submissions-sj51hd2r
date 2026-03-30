class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        mappings = defaultdict(list)

        for words in strs:

            key = self.getkey(words)

            mappings[key].append(words)
        
        return list(v for v in mappings.values())


    def getkey(self, word):
        lst = [0] * 26

        for c in word:

            index = ord(c) - ord('a')
            lst[index] += 1
        
        return tuple(lst)
        