class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        n = len(mat)
        m = len(mat[0])

        k = k % m
        
        for i in range(n):
            for j in range(m):
                shiftedIdx = (j+k) % m
                if mat[i][j] != mat[i][shiftedIdx]:
                    return False

        return True