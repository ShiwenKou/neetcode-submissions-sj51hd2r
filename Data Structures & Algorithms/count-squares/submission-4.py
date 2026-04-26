class CountSquares:

    def __init__(self):
        self.pntCnt = collections.defaultdict(int)
    def add(self, point: List[int]) -> None:
        self.pntCnt[tuple(point)] += 1
    def count(self, point: List[int]) -> int:
        res = 0
        px, py = point

        for p in self.pntCnt:
            x, y = p
            if abs(x - px) != abs(y - py) or x == px or y == py:
                continue
            res += self.pntCnt.get((x, py), 0) * self.pntCnt.get((px, y),0) * self.pntCnt[(x,y)]
        return res


        
