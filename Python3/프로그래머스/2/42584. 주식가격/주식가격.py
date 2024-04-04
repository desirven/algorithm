def solution(prices):
    answer = [0] * len(prices)
    que = []
    for i,p in enumerate(prices):
        while que and que[-1][1] > p:
            tmp = que.pop(-1)
            answer[tmp[0]] = i-tmp[0]
        que.append([i,p])
        
    while que:
        tmp = que.pop(-1)
        answer[tmp[0]] = len(prices)-tmp[0]-1
    return answer