class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        mappings = {}
        for i, c in enumerate(s):
            mappings[c] = i
        size, end = 0, 0
        res = []
        for i ,c in enumerate(s):
            size += 1
            end = max(mappings[c], end)

            if i == end:
                res.append(size)
                size = 0

        return res
