class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        from collections import defaultdict
        counter = defaultdict(list)
        for s in strs:

            freq_key = tuple(sorted(s))

            counter[freq_key].append(s)
        return list(counter.values())


        