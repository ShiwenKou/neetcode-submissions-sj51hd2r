class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        store = collections.defaultdict(list)

        for w in strs:
            key = self.genKeys(w)
            store[key].append(w)

        return list(store.values())

    
    def genKeys(self, word):
        lst = [0] * 26
        for c in word:
            index = ord(c) - ord('a')
            lst[index] += 1
        
        return tuple(lst)
        