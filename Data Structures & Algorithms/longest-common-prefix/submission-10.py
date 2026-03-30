class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        # this problem is actually not hard, we need to take the first string in the list as the default prefix.

        # we iterate rest element in the strs list

        # if prefix in not a right prefix in the next strs, we need to modify its length/ slicing.

        # here we have two techniques. one is s.startwith built-in method.

        # another one is just a index j to compare. let's now try both

        
        prefix = strs[0]

        for s in strs[1:]:

            j = 0

            while j < len(prefix) and j < len(s) and prefix[j] == s[j]:
                j += 1
            prefix = prefix[:j]

            if prefix == "":
                return prefix
        
        return prefix

