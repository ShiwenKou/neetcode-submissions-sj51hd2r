class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        

        res = {}
        for s in strs:
            freq_key = [0] * 26
            #freq_key

            for i in s:

                freq_key[ord(i) - ord('a')] += 1

            res.setdefault(tuple(freq_key), []).append(s)
        
        return list( k for i, k in res.items())




