class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        mappings = {}
        for i in range(len(s)):
            mappings[s[i]] = i

        left, right = 0, 0
        res = []
        length = 0
        for i in range(len(s)):

            right = max(mappings[s[i]],right)

            if i == right:
                res.append(right - left + 1)
                left = i + 1
        return res






