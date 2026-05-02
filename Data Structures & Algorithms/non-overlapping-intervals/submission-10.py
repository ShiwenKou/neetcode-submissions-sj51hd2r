class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        

        intervals.sort()
        
        lastEnd = intervals[0][1]
        res = 0
        for start, end in intervals[1:]:
            
            if lastEnd <= start:
                lastEnd = end
            
            else:
                res += 1
                lastEnd = min(lastEnd, end)

        return res