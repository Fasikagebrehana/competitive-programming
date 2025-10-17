class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        valid = set(range(1, n+1))

        for row in matrix:
            if set(row) != valid:
                return False
            
        for col in zip(*matrix):
            if set(col) != valid:
                return False
        
        return True