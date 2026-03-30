class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        from collections import defaultdict
        res = defaultdict(list)

        for word in strs:
            key = self.getKey(word)
            res[key].append(word)
        return list(res.values())

    def getKey(self, word):
        lst = [0]*26

        for c in word:
            idx = ord(c) - ord('a')
            lst[idx] += 1
        return tuple(lst)