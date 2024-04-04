import math
def solution(progresses, speeds):
    turn = list(math.ceil((100-a)/b) for a,b in zip(progresses, speeds))
    answer = []
    tmp,cnt = 0,0
    for t in turn:
        if t > tmp:
            answer.append(cnt)
            tmp = t
            cnt = 1
        else:
            cnt += 1
    answer.append(cnt)
    return answer[1:]