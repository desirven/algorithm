def solution(arr):
    length = max(len(arr), len(arr[0]))
    answer = [[0]*length for _ in range(length)]
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            answer[i][j] = arr[i][j]
    return answer