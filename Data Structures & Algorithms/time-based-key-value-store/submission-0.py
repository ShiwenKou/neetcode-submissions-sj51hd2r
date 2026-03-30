class TimeMap:

    def __init__(self):
        from collections import defaultdict
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:

        self.store[key].append([value,timestamp])
        

    def get(self, key: str, timestamp: int) -> str:

        res = ''

        value = self.store.get(key,[])

        left, right = (0, len(value) - 1)

        while left <= right: # consider we only have onw element in the list [0] left = right, and we also wanna check int

            mid = (left + right) // 2


            if value[mid][1] <= timestamp:

                res = value[mid][0] # potential candidate

                left = mid + 1

            else: # value[mid][1] > timestamp , we don't want from m to right
                right = mid - 1


        return res
        
