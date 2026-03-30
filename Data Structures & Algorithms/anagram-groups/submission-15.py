class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        res = defaultdict(list)


        for w in strs:

            key = self.getKey(w)
            res[key].append(w)
        return list(v for v in res.values())
        
    
    def getKey(self, s):

        lst = [0] * 26
        for c in s:
            index = ord(c) - ord('a')
            lst[index] += 1

        return tuple(lst)