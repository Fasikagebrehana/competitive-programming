class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def inbound(r, c):
            return (0 <= r < len(mat) and 0 <= c < len(mat[0]))
        
        max_height = len(mat) * len(mat[0])
        queue = deque()
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if mat[i][j] == 0:
                    queue.append((i,j))
                else:
                    mat[i][j] = max_height
        
        while queue:
            row, col = queue.popleft()
            for x, y in directions:
                newRow, newCol = row + x, col + y
                if inbound(newRow, newCol) and mat[newRow][newCol] > mat[row][col] + 1:
                    queue.append((newRow, newCol))
                    mat[newRow][newCol] = mat[row][col] + 1
        return mat