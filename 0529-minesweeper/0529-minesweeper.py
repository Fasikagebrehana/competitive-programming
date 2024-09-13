class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        # start from the click and traverse by finding 'e'
        # checking their eight sides if the is a mine
        # if there is mine change it to 1
        # else change it to 'b'
        def inbound(r, c):
            return 0 <= r < len(board) and 0 <= c < len(board[0])
        
        visited = set()
        visited.add((click[0], click[1]))

        if board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = 'X'
            return board

        directions = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]

        def dfs(r, c):

            if board[r][c] == 'E':
                count = 0
                for x, y in directions:
                    newRow, newCol = x + r, y + c
                    if inbound(newRow, newCol) and board[newRow][newCol] == 'M':
                        # print('helloooo')
                        count += 1
                if count > 0:
                    board[r][c] = str(count)

                else:
                    board[r][c] = 'B'
                    for x, y in directions:
                        newRow, newCol = x + r, y + c
                        if inbound(newRow, newCol) and board[newRow][newCol] == 'E' and (newRow, newCol) not in visited:
                            visited.add((newRow, newCol))
                            dfs(newRow, newCol)

        visited.add((click[0], click[1]))
        dfs(click[0], click[1])

        return board