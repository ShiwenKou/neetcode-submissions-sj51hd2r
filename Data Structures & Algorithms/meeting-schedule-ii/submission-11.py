"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])

        s, e = 0, 0
        cur = 0
        res = 0
        while s < len(start):

            if start[s] < end[e]:
                cur += 1
                s += 1
            
            else:
                cur -= 1
                e += 1
            
            res = max(res, cur)

        return res
