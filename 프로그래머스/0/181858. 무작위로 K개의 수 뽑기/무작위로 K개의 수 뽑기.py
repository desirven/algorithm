def solution(arr, k):
    answer = []
    for x in arr:
        if x not in answer:
            answer.append(x)
            if len(answer) >= k:
                break
    for _ in range(k-len(answer)):
        answer.append(-1)
    return answer