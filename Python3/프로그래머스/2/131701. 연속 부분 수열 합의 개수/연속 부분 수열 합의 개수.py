def solution(elements):
    answer = set(elements)
    total_len = len(elements)
    tmp = [0]*total_len
    for l in range(1, total_len+1):
        for i in range(total_len):
            tmp[i] += elements[(i+l)%total_len]
            answer.add(tmp[i])
    return len(answer)