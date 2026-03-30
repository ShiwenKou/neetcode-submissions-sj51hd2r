class Solution:

    def encode(self, strs: List[str]) -> str:


        res = []



        for i in range(len(strs)):
            res.append(str(len(strs[i]))+"#"+strs[i])
        
        return ''.join(word for word in res)

    def decode(self, s: str) -> List[str]:

        res = []
        i, j = 0, 0

        while j < len(s):

            while s[j] != '#': # j points to '#'
                j += 1

            length = int(s[i: j])

            word = s[j+1: j+1+length]

            res.append(word)

            j = j + 1 + length
            i = j
        return res




