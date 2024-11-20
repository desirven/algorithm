from collections import Counter

def solution(want, number, discount):
    wantDict = dict(zip(want, number))
    discountCounter = Counter(discount[:10])
    
    def check_sufficient():
        return all(discountCounter.get(product, 0) >= num for product, num in wantDict.items())
    
    valid_days = 0
    if check_sufficient():
        valid_days += 1
    
    for day in range(10, len(discount)):
        discountCounter[discount[day]] += 1
        discountCounter[discount[day - 10]] -= 1
        
        if discountCounter[discount[day - 10]] == 0:
            del discountCounter[discount[day - 10]]
        
        if check_sufficient():
            valid_days += 1
    
    return valid_days