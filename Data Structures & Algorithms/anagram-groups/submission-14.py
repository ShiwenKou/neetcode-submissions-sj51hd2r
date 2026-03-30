class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mappings = {}
        for i in range(len(strs)):
            key = self.getKey(strs[i])
            mappings.setdefault(key, []).append(strs[i])
        return list( l for l in mappings.values())

    def getKey(self, word):
        lst = [0] * 26

        for c in word:
            idx = ord(c) - ord('a')
            lst[idx] += 1

        return tuple(lst)