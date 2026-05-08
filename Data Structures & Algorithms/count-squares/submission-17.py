class CountSquares:

    def __init__(self):
        self.store = {}

    def add(self, point: List[int]) -> None:

        self.store[tuple(point)] = self.store.get(tuple(point), 0) + 1

    def count(self, point: List[int]) -> int:
        
        res = 0
        px, py = point
        for p in self.store:
            x, y = p

            if abs(px - x) == abs(py - y) and px != x and  py != y:

                res += self.store[(x, y)] * self.store.get((px, y), 0) * self.store.get((x, py),0)
        return res
