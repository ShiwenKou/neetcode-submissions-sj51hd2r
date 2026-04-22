class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        
        # we want rotation
        # this can be done in two passes

        # first transpose
        # mirror switch


        for i in range(len(matrix)):
            for j in range(i, len(matrix[0])):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        
        for i in range(len(matrix)):
            for j in range(len(matrix[0]) // 2):
                matrix[i][j], matrix[i][len(matrix[0]) - 1 - j] = matrix[i][len(matrix[0]) - 1 - j], matrix[i][j]