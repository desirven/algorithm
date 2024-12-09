class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []
        i = 0
        while i < len(intervals) and newInterval[0] > intervals[i][1]:
            ans.append(intervals[i])
            i+=1
        while i < len(intervals) and newInterval[1] >= intervals[i][0]:
            l = min(intervals[i][0], newInterval[0])
            r = max(intervals[i][1], newInterval[1])
            newInterval[0] = l
            newInterval[1] = r
            i += 1
        ans.append([newInterval[0], newInterval[1]])
        return ans + intervals[i:]