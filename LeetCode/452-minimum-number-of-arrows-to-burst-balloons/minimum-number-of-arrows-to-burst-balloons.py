class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if len(points)==0:
            return 0
        answer = 1
        points.sort(key = lambda x: x[1])
        s_tmp, e_tmp = points[0]
        for s,e in points[1:]:
            if e_tmp < s:
                answer += 1
                s_tmp, e_tmp = s, e
        return answer
