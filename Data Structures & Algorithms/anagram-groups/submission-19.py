class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        pattern = collections.defaultdict(list)


        def getPattern(word):

            lst = [0] * 26

            for i in range(len(word)):

                idx = ord(word[i]) - ord('a')
                lst[idx] += 1
            
            return tuple(lst)
        

        for word in strs:
            key = getPattern(word)
            pattern[key].append(word)
        
        return list(pattern.values())
