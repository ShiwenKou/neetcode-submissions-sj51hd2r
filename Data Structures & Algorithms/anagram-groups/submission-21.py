class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        

        def getKey(s):

            key = [0] * 26

            for c in s:
                idx = ord(c) - ord('a')
                key[idx] += 1

            return tuple(key)

        

        mappings = {}

        for s in strs:
            key = getKey(s)

            mappings.setdefault(key, []).append(s)

        return list(mappings.values())