class CountSquares:

    def __init__(self):
        self.counter = collections.Counter()

    def add(self, point: List[int]) -> None:
        self.counter[tuple(point)] += 1
        
    def count(self, point: List[int]) -> int:

        x, y = point
        result = 0
        for key in self.counter.keys():
            x1, y1 = key
            if abs(x - x1) == abs(y - y1) and x != x1 and y != y1:

                result += self.counter[(x1, y1)] * self.counter[(x1, y)] * self.counter[(x, y1)]

        return result


        
