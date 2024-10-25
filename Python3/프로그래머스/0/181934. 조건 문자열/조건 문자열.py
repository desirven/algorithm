def solution(ineq, eq, n, m):
    if ineq=="<":
        answer = int(n<m)
    else:
        answer = int(n>m)
    if eq=="=" and n==m:
        answer = 1
    return answer