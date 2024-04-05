def solution(arr):
    answer = [0, 0]
    
    def quard_comp(x, y, size):
        if size == 1:
            answer[arr[x][y]] += 1
            return
        
        first = arr[x][y]
        for i in range(x, x + size):
            for j in range(y, y + size):
                if arr[i][j] != first:
                    half_size = size // 2
                    quard_comp(x, y, half_size)
                    quard_comp(x, y + half_size, half_size)
                    quard_comp(x + half_size, y, half_size)
                    quard_comp(x + half_size, y + half_size, half_size)
                    return
        
        answer[first] += 1
    
    quard_comp(0, 0, len(arr))
    return answer