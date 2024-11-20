def solution(num_list):        
    return sum([countDivision(num) for num in num_list])

def countDivision(num):
    cnt = 0
    while num>=2:
        num /= 2
        cnt += 1
    return cnt