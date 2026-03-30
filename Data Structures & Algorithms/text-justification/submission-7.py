class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:

        res = []
        length = 0
        line = []

        for i in range(len(words)):

            if length + len(line) + len(words[i]) > maxWidth:

                left_spaces = maxWidth - length
                spaces = left_spaces // max(1, len(line) - 1) # the last words don't need a space
                residue = left_spaces % max(1, len(line) - 1)

                for j in range(max(len(line) - 1, 1)):
                    line[j] += ' ' * spaces
                    if residue:
                        line[j] += ' '
                        residue -= 1

                res.append(''.join(line))
                line = []
                length = 0


            line.append(words[i])
            length += len(words[i])
        
        last_line = ' '.join(line)

        trails_space = maxWidth - len(last_line)
        res.append(last_line + ' ' * trails_space)

        return res



        