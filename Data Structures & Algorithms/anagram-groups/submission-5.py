class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # firstly we iterate every elements in the strs and we generate a frequency key for each words,
        # we append each words into the hast map according their frequencies.
        counter = {}
        for s in strs:

            # generate key for s

            freq_key = ''.join(sorted(s))

            counter.setdefault(freq_key,[]).append(s)


        return list(counter.values())