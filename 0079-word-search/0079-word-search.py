class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        def inbound(r, c):
            return 0 <= r< len(board) and 0 <= c < len(board[0])

        idx = 0
        visited = set()
        
        def dfs(r, c, idx):
            if idx == len(word):
                return True
            
            for x, y in directions:
                nextR, nextC = x + r, y + c
                if inbound(nextR, nextC) and (nextR, nextC) not in visited and board[nextR][nextC] == word[idx]:

                    visited.add((nextR, nextC))
                    temp = dfs(nextR, nextC, idx + 1)
                    if temp:
                        return True
                    visited.remove((nextR, nextC))
            
        for i in range(len(board)):
            for j in range(len(board[0])):
                visited = set()
                if board[i][j] == word[0]:
                    visited.add((i, j))
                    ans = dfs(i, j, 1)
                    if ans:
                        return True
        return False