def solution(n, results):
    graph = [[0] * (n+1) for _ in range(n+1)]
    
    for a, b in results:
        graph[a][b] = 1
    
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                if graph[i][k] and graph[k][j]:
                    graph[i][j] = 1
    
    answer = 0
    for i in range(1, n+1):
        count = 0
        for j in range(1, n+1):
            if graph[i][j] or graph[j][i]:
                count += 1
        if count == n-1:
            answer += 1
    
    return answer