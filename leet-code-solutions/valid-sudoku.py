class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(set)
        col = defaultdict(set)
        sqr= defaultdict(set)
        
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                if board[i][j] in row[i] or board[i][j] in col[j] or board[i][j] in sqr[(i//3, j//3)]:
                    return False
                col[j].add(board[i][j])
                row[i].add(board[i][j])
                
                sqr[(i//3, j//3)].add(board[i][j])
        return True
        