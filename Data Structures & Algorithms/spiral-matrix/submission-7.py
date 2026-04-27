class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        topWall = 0
        rightWall = len(matrix[0])
        bottomWall = len(matrix)
        leftWall = -1
        Right, Down, Left, Up = 1, 2, 3, 4
        directions = Right
        res = []
        i, j = 0, 0
        while len(res) != len(matrix[0]) * len(matrix):

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
            elif directions == Up:
                while i > topWall:
                    res.append(matrix[i][j])
                    i -= 1
                i, j = i + 1, j + 1
                topWall += 1
                directions = Right
        return res