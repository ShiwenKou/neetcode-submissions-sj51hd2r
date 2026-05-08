class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        mappings = {}
        left, right = 0, 0
        res = []
        for i, v in enumerate(s):
            mappings[v] = i

        
        for i in range(len(s)):

            right = max(right, mappings[s[i]])

            if i == right:

                res.append(right - left + 1)
                left = i + 1
        return res
