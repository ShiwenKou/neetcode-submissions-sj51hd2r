class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        upWall = 0
        rightWall = len(matrix[0])
        bottomWall = len(matrix)
        leftWall = -1
        right, down, left, up = 1, 2, 3, 4
        directions = right
        i, j = 0, 0
        res = []
        while len(res) != len(matrix) * len(matrix[0]):

            if directions == right:
                while j < rightWall:
                    res.append(matrix[i][j])
                    j += 1
                i, j = i + 1, j - 1
                rightWall -= 1
                directions = down
            elif directions == down:
                while i < bottomWall:
                    res.append(matrix[i][j])
                    i += 1
                i, j = i - 1, j - 1
                bottomWall -= 1
                directions = left
            elif directions == left:
                while j > leftWall:
                    res.append(matrix[i][j])
                    j -= 1
                i, j = i - 1, j + 1
                directions = up
                leftWall += 1
            elif directions == up:

                while i > upWall:
                    res.append(matrix[i][j])
                    i -= 1
                i, j = i + 1, j + 1
                upWall += 1
                directions = right
        return res
