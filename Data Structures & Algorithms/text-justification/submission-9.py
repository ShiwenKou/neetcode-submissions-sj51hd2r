class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:


        res = []
        line = []
        length = 0

        for i in range(len(words)):

            if length + len(line) + len(words[i]) > maxWidth:

                spaces = maxWidth - length
                distribute = spaces // max(1, len(line) - 1)
                reminder = spaces % max(1,len(line) - 1)

                for j in range(max(1, len(line) - 1)):
                    line[j] += ' ' * distribute
                    if reminder:
                        line[j] += " "
                        reminder -= 1
                res.append(''.join(line))
                line = []
                length = 0

            line.append(words[i])
            length += len(words[i])


        lastLine = ' '.join(line)

        remains = maxWidth - len(lastLine)

        res.append(lastLine + ' ' * remains)
        return res



            

        