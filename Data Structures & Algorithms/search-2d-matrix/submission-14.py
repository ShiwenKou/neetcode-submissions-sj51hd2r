class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        left, right = 0, len(matrix) * len(matrix[0]) - 1
        mod = len(matrix[0])
        
        while left <= right:
            mid = (left + right) // 2

            # translation

            midValue = matrix[mid // mod][mid % mod]

            if midValue == target:
                return True

            if midValue > target:
                right = mid - 1
            else:
                left = mid + 1
        
        return False