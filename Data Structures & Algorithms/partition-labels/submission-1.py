class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        start = 0
        end = 0
        mappings = {}
        res = []
        for i, n in enumerate(s):
            mappings[n] = i

        for i in range(len(s)):

            new = mappings[s[i]]

            if new > end:
                end = new
            
            if i == end:
                res.append(end - start + 1)
                start = i + 1

        return res