def solution(k, tangerine):
    number_size = {}
    for size in tangerine:
        number_size[size] = number_size.get(size, 0) + 1
    number_size = list(number_size.values())
    number_size.sort(reverse=True)                   
    
    answer = 0                   
    for num in number_size:
        k -= num                 
        answer += 1
        if k<=0: 
            return answer