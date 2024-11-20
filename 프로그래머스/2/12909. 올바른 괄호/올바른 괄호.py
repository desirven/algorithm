def solution(s):
    cnt = 0
    for x in s:
        if x==')':
            cnt -= 1
            if cnt<0:
                return False
        else:
            cnt += 1
    if cnt>0:
        return False
    return True