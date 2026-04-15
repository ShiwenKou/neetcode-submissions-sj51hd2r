class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        m, n = len(matrix), len(matrix[0])

        upWall = 0
        rightWall = n
        bottomWall = m
        leftWall = -1

        Right, Down, Left, Up = 0, 1, 2, 3
        res = []
        directions = Right
        j, i = 0, 0
        while len(res) != m * n:

            if directions == Right:
                while j < rightWall:
                    res.append(matrix[i][j])
                    j += 1
                i, j = i + 1, j - 1
                rightWall -= 1
                directions = Down
            elif directions == Down:
                while i < bottomWall:
                    res.append(matrix[i][j])
                    i += 1
                i, j = i - 1, j - 1
                bottomWall -= 1
                directions = Left
            elif directions == Left:
                while j > leftWall:
                    res.append(matrix[i][j])
                    j -= 1
                i, j = i - 1, j + 1
                leftWall += 1
                directions = Up
            else:
                while i > upWall:
                    res.append(matrix[i][j])
                    i -= 1
                i, j = i + 1, j + 1
                upWall += 1
                directions = Right
        return res