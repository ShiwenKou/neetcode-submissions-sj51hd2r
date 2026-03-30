class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:

            res.append(str(len(s))+'#'+s)
        return ''.join(s for s in res)


    def decode(self, s: str) -> List[str]:


        res = []

        i, j = 0, 0
        # for char in range(len(s)):

        while j < len(s):

            
            while s[j] != '#':
                j += 1

            length = int(s[i:j]) # slicing out the length to slicing the strings

            res.append(s[j+1:j+1+length])
            i = j+1+length
            j = j+1+length
        return res





