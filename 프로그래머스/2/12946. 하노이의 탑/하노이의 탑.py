def solution(n):
    answer = []
    
    def hanoi_steps(n, source, target, tmp):
        if n == 1:
            answer.append([source, target])
            return

        hanoi_steps(n - 1, source, tmp, target)
        answer.append([source, target])
        hanoi_steps(n - 1, tmp, target, source)

    hanoi_steps(n, 1, 3, 2)
    
    return answer