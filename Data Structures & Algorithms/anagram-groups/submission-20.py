class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        def getKey(word):

            key = [0] * 26

            for i in range(len(word)):
                idx = ord(word[i]) - ord('a')
                key[idx] += 1
            
            return tuple(key)

                
        pattern = defaultdict(list)
        for word in strs:
            key = getKey(word)

            pattern[key].append(word)

        return list(pattern.values())

