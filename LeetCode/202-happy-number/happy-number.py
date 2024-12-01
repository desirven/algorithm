class Solution:
    def isHappy(self, n: int) -> bool:
        stack = []
        while n>1:
            if n in stack:
                return False
            stack.append(n)
            tmp = 0
            while n>0:
                tmp += (n%10)**2
                n //= 10
            n = tmp
        return True if n==1 else False