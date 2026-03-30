class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # we have two ways to solve this problem vertically and horizentally

        # let's now work with the horizental one.


        # horizental means we need to interate all the strings after the default prefix
        if not strs:
            return ""

        prefix = strs[0]

        for s in strs[1:]:
            j = 0

            while j < len(s) and j < len(prefix) and s[j] == prefix[j]:
                j += 1
            
            prefix = prefix[:j]

        return prefix