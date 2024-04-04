def solution(n):
    F = [0, 1]
    for _ in range(2, n+1):
        F.append(F[-1]+F[-2])        
    return F[-1]%1234567