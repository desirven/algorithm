def solution(n):
    snail = [[0 for _ in range(n)] for _ in range(n) ]
    y, x, number = -1, 0, 1
    for i, dir in zip(range(n,0,-1), [(1,0), (0,1), (-1,-1)]*(n//3+1)):
        for _ in range(i):
            y, x = y + dir[0], x + dir[1]
            snail[y][x] = number
            number += 1
    return [snail[y][x] for y in range(n) for x in range(n) if snail[y][x] != 0]