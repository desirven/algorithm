def check(s):
    stack = []
    for c in s:
        if c=="[" or c=="{" or c=="(":
            stack.append(c)
        elif c=="]" and len(stack)>0 and stack[-1]=="[":
            stack.pop()
        elif c=="}" and len(stack)>0 and stack[-1]=="{":
            stack.pop()
        elif c==")" and len(stack)>0 and stack[-1]=="(":
            stack.pop()
        else:
            return 0
    if stack:
        return 0
    else:
        return 1
    
def solution(s):
    answer = 0
    for i in range(len(s)):
        answer += check(s)
        s = s[1:] + s[0]
    return answer