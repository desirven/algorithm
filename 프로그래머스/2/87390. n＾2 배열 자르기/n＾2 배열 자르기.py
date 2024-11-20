def solution(n, left, right):
    return [max(val%n, val//n)+1 for val in range(left, right+1)]