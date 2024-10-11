def solution(clothes):
    numberItemsType = {}
    for _, t in clothes:
        if t not in numberItemsType:
            numberItemsType[t] = 1
        else:
            numberItemsType[t] += 1
    
    answer = 1
    for number in numberItemsType.values():
        answer *= number+1
        
    return answer-1