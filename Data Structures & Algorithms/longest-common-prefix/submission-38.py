class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:


        # let's try to do this again


        # this problem can be solved in two solution = the horizental one and vertical one

        # let's do vertical first


        # prefix = strs[0]

        # for i in range(len(prefix)):
        #     char = prefix[i]

        #     for s in strs[1:]:

        #         # we need to check each char

        #         if i >= len(s) or char != s[i]:
        #             return prefix[:i]
                
        # return prefix

        # now let's try the horizental solution

        prefix = strs[0]

        for s in strs[1:]:

            while not s.startswith(prefix):
                prefix = prefix[:-1]


            if prefix == "":
                return prefix
        return prefix

        