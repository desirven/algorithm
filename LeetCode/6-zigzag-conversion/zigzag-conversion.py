class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or len(s) <= numRows:
            return s
        convert_hash = {}
        row, down_flag = 0, True
        for c in s:
            if row not in convert_hash:
                convert_hash[row] = []
            convert_hash[row].append(c)
            
            if row == 0:
                down_flag = True
            elif row == numRows-1:
                down_flag = False
            
            if down_flag:
                row += 1
            else:
                row -= 1
        
        answer = ''
        for i in range(numRows):
            answer += ''.join(convert_hash[i])
        return answer