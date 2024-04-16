import heapq

def solution(n, works):
    if n >= sum(works): 
        return 0
    works = [-w for w in works]
    heapq.heapify(works)
    for _ in range(n):
        w = heapq.heappop(works)
        heapq.heappush(works, w+1)
        
    return sum([w**2 for w in works])