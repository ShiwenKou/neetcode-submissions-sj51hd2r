class CountSquares:

    def __init__(self):
        self.store = collections.defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.store[tuple(point)] += 1
        

    def count(self, point: List[int]) -> int:

        px, py = point
        res = 0
        for p in self.store:
            x, y = p

            if abs(x - px) == abs(y - py) and px != x and py != y:
                res += self.store.get((x, y), 0) * self.store.get((x, py),0) * self.store.get((px, y), 0)
        
        return res