class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        
        counter = {}

        for s in strs:
            freq_key = [0] * 26

            for i in s:
                freq_key[ord(i) - ord('a')] += 1

            counter.setdefault(tuple(freq_key),[]).append(s)
        return list(counter.values())
        