class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        output = [intervals[0]]

        for start, end in intervals[1:]:

            lastEnd = output[-1][1]

            if lastEnd < start:
                output.append([start, end])
            else:
                
                output[-1][1] = max(lastEnd, end)
        return output