class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        prefix = strs[0]


        for i in range(1, len(strs)):
            j = 0

            while j < len(strs[i]) and j < len(prefix) and prefix[j] == strs[i][j]:
                j += 1
            prefix = prefix[:j]
            
            if prefix == "":
                return prefix
        return prefix