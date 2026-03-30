class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        # how to solve this vertically?

        # we also starts with a default prefix - the first element.

        # then we reversely check the prefix index with all the other str in the list.

        # if one words don't satisfy with prefix[i] == s[i] we break, update prefix and check again

        prefix = strs[0]


        for i in range(len(prefix)):
            char = prefix[i]
            for j in range(1, len(strs)):

                if i >= len(strs[j]) or prefix[i] != strs[j][i]:
                    return prefix[:i]
        return prefix

