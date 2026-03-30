class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # firstly we iterate every elements in the strs and we generate a frequency key for each words,
        # we append each words into the hast map according their frequencies.

        from collections import defaultdict

        counter = {}

        for s in strs:

            s_key = tuple(sorted(s))

            counter.setdefault(s_key, []).append(s)
        return list(counter.values())

            


        