def solution(n, s):
    if n>s:
        return [-1]
    answer = []
    for d in range(n,0,-1):
        x = s//d
        answer.append(x)
        s, n = s-x, x
        
    return answer