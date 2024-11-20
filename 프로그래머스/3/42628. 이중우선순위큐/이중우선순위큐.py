def solution(operations):
    queue = []
    for op in operations:
        mod, num = op.split()
        if mod == 'D':
            queue = sorted(queue)
            if num == '1' and len(queue) > 0:
                del queue[-1]
            elif num == '-1' and len(queue) > 0:
                del queue[0]
        else:
            queue.append(int(num))

    if len(queue)==0:
        return [0,0]
    queue = sorted(queue)
    return [queue[-1], queue[0]]