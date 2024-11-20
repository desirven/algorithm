def solution(bridge_length, weight, truck_weights):
    answer = 1
    now_weight = []
    now = []
    while (True):
        if (not truck_weights) and (not now):
            break
        if truck_weights:
            if sum(now_weight) + truck_weights[0] <= weight:
                now_weight.append(truck_weights.pop(0))
                now.append(bridge_length)
        for i in range(len(now)):
            now[i] -= 1
        if now:
            if now[0] == 0:
                now.pop(0)
                now_weight.pop(0)
        answer += 1
    return answer