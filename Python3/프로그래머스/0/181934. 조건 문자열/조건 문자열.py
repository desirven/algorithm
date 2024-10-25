def solution(ineq, eq, n, m):
    if eq=="=" and n==m:
        return 1
    if ineq=="<":
        answer = int(n<m)
    else:
        answer = int(n>m)
    return answer 