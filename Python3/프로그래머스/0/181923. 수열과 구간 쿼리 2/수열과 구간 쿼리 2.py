def solution(arr, queries):
    answer = []
    for (s,i,k) in queries:
        selected_arr = [x for x in arr[s:i+1] if x>k]
        if len(selected_arr)==0:
            answer.append(-1)
        else:
            answer.append(min(selected_arr))
    return answer