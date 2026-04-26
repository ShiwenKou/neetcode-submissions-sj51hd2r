class CountSquares:

    def __init__(self):
        self.pntCnt = collections.defaultdict(int)
        self.pntList = []
    def add(self, point: List[int]) -> None:
        self.pntCnt[tuple(point)] += 1
        self.pntList.append(point)

    def count(self, point: List[int]) -> int:
        res = 0
        px, py = point

        for p in self.pntList:
            x, y = p
            if abs(x - px) != abs(y - py) or x == px or y == py:
                continue
            res += self.pntCnt[(x, py)] * self.pntCnt[(px, y)]
        return res


        
