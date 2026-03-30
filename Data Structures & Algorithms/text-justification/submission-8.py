class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        line = []
        length = 0

        for i in range(len(words)):

            # here we need a if condition to see if the current line exceeds the maxWidth

            if length + len(line) + len(words[i]) > maxWidth: # if it is about to exceeds we join the line & reset

                extra_space = maxWidth - length
                spaces = extra_space // max(1, len(line) - 1)
                remainder = extra_space % max(1, len(line)- 1)
                for j in range(max(1,len(line) - 1)):
                    line[j] += " " * spaces

                    if remainder:
                        line[j] += ' '
                        remainder -= 1
                
                res.append(''.join(line))
            
                line = []
                length = 0

            # each time we put the value of index i into the line

            line.append(words[i])
            length += len(words[i]) # we sum up the total length
            i += 1 

        # the last word will not be added in if
        last_line = ' '.join(line)
        trail_space = maxWidth - len(last_line)

        last_line += ' ' * trail_space
        res.append(last_line)
        

        return res