class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])

        ans = []
        RIGHT, DOWN, LEFT, UP = 0, 1, 2, 3
        directions = RIGHT
        upWall = 0
        rightWall = n
        bottomWall = m
        leftWall = -1
        i, j = 0, 0
        while len(ans) != m * n:

            if directions == RIGHT:
                while j < rightWall:
                    ans.append(matrix[i][j])
                    j += 1
                i, j = i + 1, j - 1
                rightWall -= 1
                directions = DOWN
            elif directions == DOWN:
                while i < bottomWall:
                    ans.append(matrix[i][j])
                    i += 1
                i, j = i - 1, j - 1
                bottomWall -= 1
                directions = LEFT
            elif directions == LEFT:
                while j > leftWall:
                    ans.append(matrix[i][j])
                    j -= 1
                i, j = i - 1, j + 1
                leftWall += 1
                directions = UP
            else: 
                while i > upWall:
                    ans.append(matrix[i][j])
                    i -= 1
                i, j = i + 1, j + 1
                upWall += 1
                directions = RIGHT
        return ans

