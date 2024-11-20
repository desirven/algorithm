from collections import deque

def solution(n, edge):
    graph = [[] for _ in range(n+1)]
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)

    distance = [0 for _ in range(n+1)]
    distance[1] = 1

    node_queue = deque([1])

    while node_queue:
        current_node = node_queue.popleft()
        for target_node in graph[current_node]:
            if distance[target_node] == 0:
                node_queue.append(target_node)
                distance[target_node] = distance[current_node] + 1

    return distance.count(max(distance))