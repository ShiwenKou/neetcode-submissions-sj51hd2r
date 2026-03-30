class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # firstly we iterate every elements in the strs and we generate a frequency key for each words,
                # we append each words into the hast map according their frequencies.
        from collections import defaultdict

        counter = defaultdict(list)

        for s in strs:
            freq = Counter(s)
            # Sort by character to create consistent key
            freq_key = tuple(sorted(freq.elements()))  # ('a', 'a', 'b')

            counter[freq_key].append(s)

        return list(counter.values())


        