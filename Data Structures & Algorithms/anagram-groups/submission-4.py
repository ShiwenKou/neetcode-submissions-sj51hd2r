class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # firstly we iterate every elements in the strs and we generate a frequency key for each words,
        # we append each words into the hast map according their frequencies.

        from collections import defaultdict, Counter

        counter = defaultdict(list)

        for s in strs:

            freq_key = tuple(sorted(s))

            counter[freq_key].append(s)
        
        return list([counter.values()][0])