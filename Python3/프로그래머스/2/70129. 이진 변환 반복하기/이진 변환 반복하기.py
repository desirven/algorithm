def solution(s):
    x = s
    zero_cnt, cnt = 0, 0
    while True:
        zero_cnt += x.count('0')
        c = x.count('1')
        x = bin(c)[2:]
        cnt += 1
        if x == '1':
            break
    return [cnt, zero_cnt]