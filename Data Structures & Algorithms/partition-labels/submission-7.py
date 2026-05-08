class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        left, right = 0, 0

        res = []
        mappings = {}
        for i, c in enumerate(s):
            mappings[c] = i

        for i in range(len(s)):

            right = max(right, mappings[s[i]])

            if i == right:
                
                res.append(right - left + 1)
                left = i + 1
        return res
