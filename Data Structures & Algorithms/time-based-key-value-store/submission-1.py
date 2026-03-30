class TimeMap:

    def __init__(self):
        # {key: [value timestamp]}
        from collections import defaultdict
        self.d = defaultdict(list)
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d[key].append([value, timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        # is timestamp exists
        res = ''

        value = self.d[key] # if key is missing, return [], 
        # [[value, timestamp], [value, timestamp]...]

        left, right = 0, len(value) - 1

        while left <= right: # we are doing search. so each should check

            mid = (left + right ) // 2
            if value[mid][1] <= timestamp: # potential candidate

                res = value[mid][0]
                left = mid + 1
            else:
                right = mid - 1
        return res


        
