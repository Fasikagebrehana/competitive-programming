class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open, closed = 0, 0
        moves = 0
        stack = []
        for i in range(len(s)):
            if s[i] == '(':
                open += 1
            else:
                if open > 0:
                    open -= 1
                else:
                    moves += 1
        
        if open > 0:
            moves += open
        return moves