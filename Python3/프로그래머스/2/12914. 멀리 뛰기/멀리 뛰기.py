def solution(n):
    if n in [1,2]:
        return n
    
    F = [1, 2]
    for _ in range(2, n):
        F.append(F[-1] + F[-2])
    return F[-1]%1234567