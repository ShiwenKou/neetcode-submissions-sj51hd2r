class CountSquares:

    def __init__(self):
        self.store = collections.defaultdict(int)

    def add(self, point: List[int]) -> None:

        self.store[tuple(point)] += 1
        
    def count(self, point: List[int]) -> int:


        px, py = point
        res = 0
        for node in self.store:

            x, y = node

            if abs(px - x) == abs(py - y) and px != x and py != y:

                res += self.store[(x, y)] * self.store.get((x, py), 0) * self.store.get((px, y), 0)
        return res

