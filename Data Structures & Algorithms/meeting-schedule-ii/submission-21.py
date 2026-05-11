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
        cnt = 0
        res = 0
        while s < len(start):
            if start[s] < end[e]: # 如果一个最近的会议开始时间，早于最近一个会议的结束时间，我们就需要新安排一个房间
                s += 1
                cnt += 1

            else: # 如果在最近一个开始时间前，有一个已有会议结束了，那我们就可以减少一个已经安排的会议房间
                e += 1
                cnt -= 1
            res = max(res, cnt)
        return res