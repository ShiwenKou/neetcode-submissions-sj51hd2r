class CountSquares:

    def __init__(self):
        self.Counter = defaultdict(int)
        self.points = []
    def add(self, point: List[int]) -> None:
        self.Counter[tuple(point)] += 1
        self.points.append(point)

    def count(self, point: List[int]) -> int:

        res = 0
        px, py = point
        for p in self.points:
            x, y = p
            if abs(x - px) != abs(y - py) or (x == px and y == py):
                continue
            
            res += self.Counter[(x, py)] * self.Counter[(px, y)]

        return res
        
