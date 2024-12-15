class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num, res, sign = 0, 0, 1 
        for c in s:
            if c.isdigit():
                num = num * 10 + (ord(c) - ord('0'))
            elif c in ['-', '+']:
                res += num * sign
                num = 0
                sign = 1 if c=='+' else -1
            elif c == '(':
                stack.append(res)
                stack.append(sign)
                res, sign = 0, 1
            elif c == ')':
                res += num * sign 
                num, sign = 0, 1 
                res *= stack.pop()
                res += stack.pop()
        
        if num != 0:
            res += num * sign 
        
        return res 