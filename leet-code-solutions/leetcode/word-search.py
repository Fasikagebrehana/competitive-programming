class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row = len(board)
        col = len(board[0])
        visited = set()
        def helper(idx, i, j):
            if idx == len(word):
                return True
            if i >= row or i < 0 or j < 0 or  j >= col:
                return
            if (i, j) in visited:
                return
            if word[idx] != board[i][j]:
                return False
            
            visited.add((i, j))
            if helper(idx + 1, i, j + 1):
                return True
            if helper(idx + 1, i+1, j):
                return True
            if helper(idx + 1, i-1, j):
                return True
            if helper(idx + 1, i, j-1):
                return True
            visited.remove((i, j))
            return False
        for r in range(row):
            for c in range(col):
                if board[r][c] == word[0]:
                    if helper(0, r, c):
                        return True
        return False