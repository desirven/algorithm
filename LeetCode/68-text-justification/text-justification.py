class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []
        current_line = []
        current_length = 0

        for word in words:
            if current_length + len(word) + len(current_line) <= maxWidth:
                current_line.append(word)
                current_length += len(word)
            else:
                if len(current_line) == 1:
                    result.append(current_line[0] + ' ' * (maxWidth - current_length))
                else:
                    spaces = maxWidth - current_length
                    space_between = spaces // (len(current_line) - 1)
                    extra_spaces = spaces % (len(current_line) - 1)
                    line = ''
                    for i, w in enumerate(current_line[:-1]):
                        line += w + ' ' * space_between
                        if i < extra_spaces:
                            line += ' '
                    line += current_line[-1]
                    result.append(line)
                
                current_line = [word]
                current_length = len(word)
        
        last_line = ' '.join(current_line)
        result.append(last_line + ' ' * (maxWidth - len(last_line)))

        return result