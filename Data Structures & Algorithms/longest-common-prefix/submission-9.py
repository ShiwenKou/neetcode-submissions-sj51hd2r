class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        # this problem we need to use the first element in the list as the default prefix

        # then we iterate from the second element to the last

        # if current prefix is the common prefix we continue the for loop

        # else we slice the prefix then compare again. use while here


        prefix = strs[0]

        for i in range(1, len(strs)):


            # how to know if a str contains another str?
            # we need to iterate each char in the prefix and to see if it exist in the other str

            j = 0
            while j < len(prefix) and len(strs[i]) > j and prefix[j] == strs[i][j]:
                    
                j += 1
            prefix = prefix[:j]

        return prefix