def solution(n, computers):
    def BFS(current_node):
        prev_list.append(current_node)
        for next_node in range(len(computers[current_node])):
            if computers[current_node][next_node]==1 and next_node not in prev_list:
                BFS(next_node)

    answer = 0
    prev_list = []
    for node in range(n):
        if node not in prev_list:
            BFS(node)
            answer += 1
    return answer