class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        # rewrite again
        # the horizental: we iterate the strs list and shirnk the prefix

        # the vertical : we iterate the prefix direct return if condition not matched.
            # prefix index i cannot greater than other elements. 
            # when prefix[i] no longer == other elements[i] we direct return

        prefix = strs[0]

        for i in range(1, len(strs)):

            while not strs[i].startswith(prefix):
                prefix = prefix[:-1]
            
            if prefix == "":
                return prefix
        return prefix

