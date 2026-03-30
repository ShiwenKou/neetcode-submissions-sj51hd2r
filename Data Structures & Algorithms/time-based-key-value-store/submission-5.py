class TimeMap:

    def __init__(self):
        self.store = collections.defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append([value, timestamp])
        
    def get(self, key: str, timestamp: int) -> str:

        candidates = self.store[key] #[[value, timestap],[],[]]
        # search based on the second key

        left, right = 0, len(candidates) - 1
        res = ''
        while left <= right:
            mid = (left + right) // 2

            if candidates[mid][1] == timestamp:
                return candidates[mid][0]

            if candidates[mid][1] > timestamp:
                right = mid - 1
            else:
                res = candidates[mid][0]
                left = mid + 1
        return res

        
