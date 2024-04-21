class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def inbound(r, c):
            return (0 <= r < len(board) and 0 <= c < len(board[0]))
        queue = deque()
        visited = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O' and (i == 0 or i == len(board) - 1 or j == 0 or j == len(board[0]) - 1):
                    queue.append((i,j))
                    visited.add((i,j))

        while queue:
            row, col = queue.popleft()
            for x, y in directions:
                newRow, newCol = row + x, col + y
                if inbound(newRow, newCol) and board[newRow][newCol] == 'O' and (newRow, newCol) not in visited:
                    queue.append((newRow, newCol))
                    visited.add((newRow, newCol))
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O' and (i, j) not in visited:
                    board[i][j] = 'X'