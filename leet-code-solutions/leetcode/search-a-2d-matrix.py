class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        col = (len(matrix[0]))
        row = len(matrix)
        low = 0
        high = (row * col) - 1
        
        while low <= high:
            mid = (low + high) // 2
            if matrix[mid//col][mid%col] == target:
                return True
            elif matrix[mid//col][mid%col] > target:
                high = mid - 1
            else:
                low = mid + 1
        return False

            