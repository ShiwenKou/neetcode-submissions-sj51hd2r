class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        

        def getKey(word):

            key = [0] * 26

            for char in word:

                idx = ord(char) - ord('a')

                key[idx] += 1
            
            return tuple(key)

        mappings = {}

        for word in strs:

            key = getKey(word)

            mappings.setdefault(key, []).append(word)

        return list(mappings.values())
        