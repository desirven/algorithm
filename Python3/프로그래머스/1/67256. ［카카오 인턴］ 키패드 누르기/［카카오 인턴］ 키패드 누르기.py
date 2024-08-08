def solution(numbers, hand):
    def cal_dist(num, now_l, now_r, pos):
        dist_l = abs(pos[now_l][0] - pos[num][0]) + abs(pos[now_l][1] - pos[num][1])
        dist_r = abs(pos[now_r][0] - pos[num][0]) + abs(pos[now_r][1] - pos[num][1])
        if dist_l == dist_r:
            return 'R' if hand == 'right' else 'L'
        return 'R' if dist_l > dist_r else 'L'

    position = {1:(0, 0), 2:(0, 1), 3:(0, 2),
                4:(1, 0), 5:(1, 1), 6:(1, 2),
                7:(2, 0), 8:(2, 1), 9:(2, 2),
                '*':(3, 0), 0:(3, 1), '#':(3, 2)}
    left, right = set([1,4,7]), set([3,6,9])
    now_l, now_r = '*', '#'
    result = ''
    
    for num in numbers:
        if num in left: 
            result += 'L'
            now_l = num
        elif num in right: 
            result += 'R'
            now_r = num
        else: 
            result += cal_dist(num, now_l, now_r, position)
            if result[-1] == 'L':
                now_l = num
            else :
                now_r = num
    
    return result