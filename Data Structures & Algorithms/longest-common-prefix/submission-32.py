class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        # rewrite again
        # the horizental: we iterate the strs list and shirnk the prefix

        # the vertical : we iterate the prefix direct return if condition not matched.
            # prefix index i cannot greater than other elements. 
            # when prefix[i] no longer == other elements[i] we direct return
        if not strs:
            return ""
        prefix = strs[0]

        # for i in range(1, len(strs)):

        #     while not strs[i].startswith(prefix):
        #         prefix = prefix[:-1]
            
        #     if prefix == "":
        #         return prefix
        # return prefix

        for i in range(len(prefix)):

            for j in range(1,len(strs)):

                if i >= len(strs[j]) or prefix[i] != strs[j][i]:
                    return prefix[:i]
        return prefix
