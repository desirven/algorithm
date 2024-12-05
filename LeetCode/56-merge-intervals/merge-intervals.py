class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])
        answer = [intervals[0]]
        for interval in intervals[1:]:
            s, e = interval
            if answer[-1][1] < s:
                answer.append(interval)
            else:
                answer[-1][1] = max(answer[-1][1], e)
        return answer