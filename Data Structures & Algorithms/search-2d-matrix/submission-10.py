class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # for this problem we have two ways to solve, one is do two binary search independently
        # one to look for the row num and another to find the colunm


        top, bottom = (0, len(matrix)- 1)

        while top <= bottom:

            middle = (top + bottom) // 2

            if target > matrix[middle][-1]:
                top = middle + 1

            elif target < matrix[middle][0]:
                bottom = middle - 1
            else:
                break
        if top > bottom:
            return False
        

        left, right = (0, len(matrix[0]))

        while left <= right:
            m = (left + right) // 2

            if target > matrix[middle][m]:
                left = m + 1
            elif target < matrix[middle][m]:
                right = m - 1
            else:
                return True
        return False