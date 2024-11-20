def solution(survey, choices):
    type = {'RT':0, 'CF':0, 'JM':0, 'AN':0}
    for s,c in zip(survey, choices):
        if s[0] > s[1]:
            s = s[1] + s[0]
            c = 8 - c
        type[s] += (c-4)
    
    answer=''
    for k,v in type.items():
        if v <= 0 :
            answer += k[0]
        else : 
            answer += k[1]
    
    return answer