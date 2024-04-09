from collections import deque

def find_min_cost(graph, start, max_cost):
    costs = [max_cost for _ in range(len(graph))]
    node_queue = deque([(start, 0)])
    costs[start] = 0

    while node_queue:
        current_node, current_cost = node_queue.popleft()

        if costs[current_node] < current_cost:
            continue

        for next_node, next_cost in graph[current_node]:
            cost = current_cost + next_cost
            if cost < costs[next_node]:
                costs[next_node] = cost
                node_queue.append((next_node, cost))

    return costs

def solution(n, s, a, b, fares):
    max_cost = n * 100000 + 1
    graph = [[] for _ in range(n+1)]

    for node1, node2, cost in fares:
        graph[node1].append((node2, cost))
        graph[node2].append((node1, cost))

    s_costs = find_min_cost(graph, s, max_cost)
    a_costs = find_min_cost(graph, a, max_cost)
    b_costs = find_min_cost(graph, b, max_cost)

    answer = max_cost
    for i in range(1, n+1):
        answer = min(answer, s_costs[i] + a_costs[i] + b_costs[i])

    return answer