class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        row_len  = len(matrix)
        col_len = len(matrix[0])

        left = 0
        right = row_len * col_len - 1

        while left <= right:
            m = (left + right) // 2

            row = m // col_len

            col = m % col_len

            if matrix[row][col] > target:
                right = m - 1
            elif matrix[row][col] < target:
                left = m + 1
            else:
                return True
        return False
        