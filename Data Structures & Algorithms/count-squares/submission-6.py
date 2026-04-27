class CountSquares:

    def __init__(self):
        
        self.pntCnt = collections.defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.pntCnt[tuple(point)] += 1
        

    def count(self, point: List[int]) -> int:
        px, py = point
        res = 0
        for p in self.pntCnt:
            x, y = p

            if abs(px - x) != abs(py - y) or x == px or y == py:
                continue

            res += self.pntCnt.get((x, y), 0) * self.pntCnt.get((x, py), 0) * self.pntCnt.get((px, y), 0)
        return res


        
