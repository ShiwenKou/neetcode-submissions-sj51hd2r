class CountSquares:

    def __init__(self):
        self.pnt = collections.defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.pnt[tuple(point)] += 1
        
    def count(self, point: List[int]) -> int:

        x, y = point
        res = 0
        for px, py in self.pnt:
            if abs(px - x) != abs(py - y) or px == x or py == y:
                continue
            
            res += self.pnt.get((px, py), 0) * self.pnt.get((px, y), 0) * self.pnt.get((x, py), 0)

        return res

        
