class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        merged = []
        i = 0
        
        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            merged.append(intervals[i])
            i += 1
    
        while i < len(intervals) and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            print(i)
            print(newInterval[0])
            print(newInterval[1])
            i += 1
    
        merged.append(newInterval)
    
        while i < len(intervals):
            merged.append(intervals[i])
            i += 1
    
        return merged