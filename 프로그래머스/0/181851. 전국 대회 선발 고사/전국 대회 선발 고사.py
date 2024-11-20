def solution(rank, attendance):
    answer = []
    for rnk in range(1, len(rank)+1):
        idx = rank.index(rnk)
        if attendance[idx]:
            answer.append(idx)
        if len(answer)>=3:
            break
    return answer[0]*10000 + answer[1]*100 + answer[2]